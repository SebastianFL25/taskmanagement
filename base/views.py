
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.sessions.models import Session
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken

from .api.serializer import CustomTokenObtainPairSerializer,UserSerializers
from django.contrib.auth import authenticate
from rest_framework.generics import GenericAPIView
from .models import User


class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    
    """def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)
        if user:
            return self.post(request, *args, **kwargs)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)"""
    
    def post(self, request, *args, **kwargs):
        
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(
            email=email,
            password=password
        )
        
        if user:
            login_serializer = self.serializer_class(data=request.data)
            
            if login_serializer.is_valid():
                
                user_serializer= UserSerializers(user)
                Response({
                    'token':login_serializer.validated_data.get('access'),
                    'refresh-token':login_serializer.validated_data.get('refresh'),
                    'user':user_serializer.data,
                    'message':'Inicio de sesion Exitoso'
                },status=status.HTTP_200_OK)
                
            print(login_serializer.errors)
            return Response({'error':'Email o contraseña incorrectoss'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'Email o contraseña incorrectos'},status=status.HTTP_400_BAD_REQUEST)
        
class TokenRefreshView(TokenRefreshView):
    pass

        
class Logout(GenericAPIView):
    
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('user',''))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message':'Sesion Cerrada Correctamente'},status=status.HTTP_200_OK)
        return Response({'message':'No existe este usuario'},status=status.HTTP_400_BAD_REQUEST)
        
