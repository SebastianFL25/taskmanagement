
from datetime import datetime
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from .api.serializer import CustomTokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .api.serializer import  UserSerializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.sessions.models import Session

from .models import User
class Login(TokenObtainPairView):
    serializer_class=CustomTokenObtainPairSerializer
    
    
    def post(self,request,*args, **kwargs):
        
        email = request.data.get('email','')
        password = request.data.get('password','')
        
        user= authenticate(
            email=email,
            password=password
        )
        
        if user :
            login_seializer = self.serializer_class(data=request.data)
            if login_seializer.is_valid():
                user_serializer = UserSerializers(user)
                return Response({
                    'token':login_seializer.validated_data.get("access"),
                    'refresh-token': login_seializer.validated_data.get("refresh"),
                    'user':user_serializer.data,
                    'message':'Login access succesful'
                },status=status.HTTP_200_OK)
            return Response({'error':'Email or password incorrect'},status=status.HTTP_401_UNAUTHORIZED)

        return Response({'error':'Email or password incorrect'},status=status.HTTP_401_UNAUTHORIZED)

class Logout(GenericAPIView):
    def post(self,request,*args, **kwargs):
        user = User.objects.filter(email=request.data.get('email',None))
        if user.exists():
            RefreshToken.for_user(user.first())

            return Response({'message':'Session close'},status=status.HTTP_200_OK)
        return Response({'error':'No exist this user'},status=status.HTTP_401_UNAUTHORIZED)

"""from .api.serializer import CustomAuthTokenSerializer
from django.contrib.sessions.models import Session
from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.views import APIView
from .models import User


class ObtainAuthTokenp(APIView):
    throttle_classes = ()
    permission_classes = ()
    parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    renderer_classes = (renderers.JSONRenderer,)
    serializer_class = CustomAuthTokenSerializer

    if coreapi_schema.is_enabled():
        schema = ManualSchema(
            fields=[
                coreapi.Field(
                    name="email",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="email",
                        description="Valid email for authentication",
                    ),
                ),
                coreapi.Field(
                    name="password",
                    required=True,
                    location='form',
                    schema=coreschema.String(
                        title="Password",
                        description="Valid password for authentication",
                    ),
                ),
            ],
            encoding="application/json",
        )

    def get_serializer_context(self):
        return {
            'request': self.request,
            'format': self.format_kwarg,
            'view': self
        }

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


#obtain_auth_token = ObtainAuthToken.as_view()



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
                    #all_session =Session.objects.filter(expire_date__gte =datetime.now())
                    #if all_session.exists():
                    #    for session in all_session:
                    #       session_data = session.get_decoded()
                    #        if user.id == int(session_data.get('_auth_user_id')):
                    #            session.delete()
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
"""