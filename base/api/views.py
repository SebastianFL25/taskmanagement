from django.http import Http404
from .serializer import UserSerializers,UserUpdateSerializer,UserRDSerializers,PaswordSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView,RetrieveDestroyAPIView,ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from base.models import User
from django.shortcuts import get_object_or_404


class CreateGenericView(CreateAPIView):
    serializer_class = UserSerializers
    
    def post(self,request):
        serializers = self.serializer_class(data = request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response({'message':'User created successfully'},status= status.HTTP_201_CREATED)
        return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)


class LisGenericAPIView(ListAPIView):
    
    serializer_class=UserSerializers
    queryset = User.objects.all().filter(is_active=True)
    
    
class UpdateGenericAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    
    queryset= User.objects.filter(is_active=True)
    
class RetrieveDestroyGenericAPIView(RetrieveDestroyAPIView):
    serializer_class = UserRDSerializers
    
class RetrieveDestroyGenericAPIView(RetrieveDestroyAPIView):
    serializer_class = UserRDSerializers        
    
    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(is_active=True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id=pk, is_active=True).first()
        
    def delete(self, request, pk=None):
        user = self.get_queryset(pk=pk)
        if user:
            user.is_active = False
            user.save()
            return Response({'message': 'Usuario eliminado correctamente'}, status=status.HTTP_200_OK) 
        return Response({'message': 'Usuario no encontrado'}, status=status.HTTP_400_BAD_REQUEST)

class Password(APIView):
    
    def get_object(self, pk=None):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        
    def post(self,request,pk=None,format=None):
        user = self.get_object(pk)
        password_serializer= PaswordSerializer(data=request.data)
        if password_serializer.is_valid():
            user.set_password(password_serializer.validated_data['password'])
            user.save()
            return Response({'message':'contraseña actualizada'})
        print(password_serializer.errors)
        return Response({'error_message':'errores en la informacion enviada'})

    
     
    
    