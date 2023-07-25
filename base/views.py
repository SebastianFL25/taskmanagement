
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from django.contrib.sessions.models import Session

from .api.serializer import  UserSerializers
from rest_framework.views import APIView
from .models import User
from .utils import ObtainAuthTokenp
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class UserTokenRefresh(APIView):
    def get(self,request,*args, **kwargs):
        email= request.GET.get('email')
        try:
            user_token=Token.objects.get(
                user= UserSerializers().Meta.model.objects.filter(email=email).first()
            )
            return Response({
                'token':user_token.key
            })
        except:
            return Response(
                {'error':'Credential incorrect'},status=status.HTTP_400_BAD_REQUEST 
            ) 

class Login(ObtainAuthTokenp):
    #authentication_classes = [TokenAuthentication]
    #permission_classes = [IsAuthenticated]
    
    def post(self, request):
        
        
        loginserializer = self.serializer_class(data=request.data,context={"request":request})
        if loginserializer.is_valid():
            user =loginserializer.validated_data['user']
            if user.is_active:
                
                token,created = Token.objects.get_or_create(user = user)
                user_tokenserializers= UserSerializers(user)
                if created:
                    return Response({
                        "Token": token.key,
                        "user":user_tokenserializers.data,
                        "message":"Login successful"
                    },status= status.HTTP_201_CREATED)
                    
                else:
                    """all_session =Session.objects.filter(expire_date__gte =datetime.now())
                    if all_session.exists():
                        for session in all_session:
                            session_data = session.get_decoded()
                            if user.id == int(session_data.get('_auth_user_id')):
                                session.delete()"""
                    token.delete()
                    #token =Token.objects.create(user=user)
                    return Response({
                        "message":"The user is already logged in"
                    },status= status.HTTP_409_CONFLICT)
            else:
                return Response({'error':'can not enter'},status=status.HTTP_401_UNAUTHORIZED)
        else: 
            return Response({'error':'Incorrect username or password'},status=status.HTTP_401_UNAUTHORIZED)
        
        
class Logout(APIView):
    def post(self, request, *args, **kwargs):
        try:
            token = request.POST.get('token')
            token = Token.objects.filter(key=token).first()
            print(token.user)
            if token:
                user = token.user
                all_session =Session.objects.filter(expire_date__gte =datetime.now())
                if all_session.exists():
                    for session in all_session:
                        session_data = session.get_decoded()
                        if user.id == int(session_data.get('_auth_user_id')):
                            session.delete()
            
                token.delete()
                
                session_message = 'User session deleted'
                token_message = 'Token deleted'
                    
                return Response({'session_message':session_message,'token_message':token_message}, status=status.HTTP_200_OK)
            return Response({'error_message':'User does not exist'},status=status.HTTP_400_BAD_REQUEST)
        except:    
            return Response({'error_message':'No token found in the request'},status=status.HTTP_409_CONFLICT)
