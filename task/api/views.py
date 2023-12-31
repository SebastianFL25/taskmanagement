#from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializerModel,StatusSerializerModel,TaskUpdateSerializerModel,TaskAssingToNewUserSerializer,TaskStatusSerializer,TaskStatSerializer
from task.models import Task,Status
from rest_framework.response import Response
#from rest_framework import status
from rest_framework import generics
from rest_framework.authtoken.views import Token
#from base.authentication_mixin import Authentications
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from base.models import User

class TaskUpdate(generics.RetrieveUpdateAPIView):

    serializer_class = TaskUpdateSerializerModel
    queryset= queryset =Task.objects.all()
    

class TaskModelViewSet(ModelViewSet):
    #authentication_classes = [Authentications]
    permission_classes=(IsAuthenticated,)
    
    serializer_class = TaskSerializerModel
    queryset = Task.objects.all()
    
    def get_serializer_class(self):
        for key ,value in self.request.__dict__.items():
            print(key,'==',value)
        if self.request.method in ['GET','POST','PUT']:
            return TaskSerializerModel
        else:
            return TaskUpdateSerializerModel
        
    """def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        mensaje = {'mensaje': 'Tarea eliminada'}
        return Response(mensaje, status=status.HTTP_204_NO_CONTENT)"""
    
    
    """def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.all()
        return self.get_serializer().Meta.model.objects.filter(id=pk)
    
    def list(self,request,*args, **kwargs):
        
        serializer = self.get_serializer(data=self.get_queryset(),many=True)
        if serializer.is_valid():
            
            
            return Response({'lista':'lista'},serializer.data,status=status.HTTP_200_OK)
        return Response(serializer)
        
    def pacth(self,request,pk= None):
        if self.get_queryset(pk):
            serializer = self.get_serializer(self.get_queryset(pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message':'task not exist'},status=status.HTTP_404_NOT_FOUND)
    
    def update(self,request,pk=None):
        serializer_class = TaskUpdateSerializerModel
        
        data= serializer_class.Meta.model.objects.filter(id=pk)
        
        if data:
            serializer = serializer_class(data,data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response('errors',status=status.HTTP_400_BAD_REQUEST)"""

class TaskAssingToNewUser(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Task.objects.all()
    serializer_class=TaskAssingToNewUserSerializer
    

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TaskSerializerModel
        else:
            return TaskStatusSerializer
    
    
class TaskStatus(generics.RetrieveUpdateAPIView):
    lookup_field = "id"
    queryset = Task.objects.all()
    serializer_class=TaskAssingToNewUserSerializer
    

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return TaskSerializerModel
        else:
            return TaskAssingToNewUserSerializer

class StatusLisCreateApiView(generics.ListCreateAPIView):
    #authentication_classes = [SessionAuthentication]
    #permission_classes = [IsAuthenticated]
    serializer_class=StatusSerializerModel
    queryset= Status.objects.all()
    
    
class Stat(APIView):

    def get(self,request,pk=None):
        
        try:
            user = User.objects.get(id=pk)
            
                
            user_email=user.email
            
            total_task = Task.objects.filter(user_id=pk).count()
            task_completed = Task.objects.filter(user_id=pk,status=3).count()
            task_pending = Task.objects.filter(user_id=pk,status=1).count()
            task_in_progress =Task.objects.filter(user_id=pk,status=2).count()
            
            estadisticas = {
                'user':user_email,
                'total_task': total_task,
                'task_completed': task_completed,
                'task_pending': task_pending,
                'task_in_progress': task_in_progress
            }
            
            serializer = TaskStatSerializer(estadisticas)
            return Response(serializer.data)
        except User.DoesNotExist:
         
            return Response({'error_message':'User not exist'})
        
        
        
        
        
    
 

   