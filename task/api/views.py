from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializerModel,StatusSerializerModel,TaskUpdateSerializerModel,TaskAssingToNewUserSerializer,TaskStatusSerializer
from task.models import Task,Status
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authtoken.views import Token
from base.authentication_mixin import Authentications
from rest_framework.views import APIView


class TaskUpdate(generics.RetrieveUpdateAPIView):

    serializer_class = TaskUpdateSerializerModel
    queryset= queryset =Task.objects.all()
    

class TaskModelViewSet(ModelViewSet):
    authentication_classes = [Authentications]

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
    
    def get(self, request,format=None):
        user = request.user  # Obtiene el usuario autenticado
        tasks = Task.objects.filter(user=user)  # Filtra las tareas del usuario
        total_tasks = tasks.count()  # Calcula la cantidad total de tareas
        completed_tasks = tasks.filter(status=Status.objects.filter(name='Completed')).count()  # Calcula la cantidad de tareas completadas
        pending_tasks = tasks.filter(status=Status.objects.filter(name='In Progress')).count()  # Calcula la cantidad de tareas pendientes
        
        print(user)
        # Crea un diccionario con las estadísticas
        stats = {
            'total_tasks': total_tasks,
            'completed_tasks': completed_tasks,
            'pending_tasks': pending_tasks
        }
        
        return Response(stats)
        
    
 

   