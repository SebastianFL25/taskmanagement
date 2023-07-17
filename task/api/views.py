from rest_framework.viewsets import ModelViewSet
from .serializers import TaskSerializerModel,StatusSerializerModel
from task.models import Task,Status
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import generics


class TaskModelViewSet(ModelViewSet):
    serializer_class = TaskSerializerModel
    queryset = Task.objects.all()
    
    def get_queryset(self,pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter()
        return self.get_serializer().Meta.model.objects.filter(id=pk)
    
    def list(self,request):
        
        serializer = self.serializer_class(data=self.get_queryset(),many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
        
    def pacth(self,request,pk= None):
        if self.get_queryset(pk):
            serializer = self.serializer_class(self.get_queryset(pk))
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response({'message':'task not exist'},status=status.HTTP_404_NOT_FOUND)
    
    def put(self,request,pk=None):
        data = self.get_queryset(pk)
        if data:
            serializer = self.serializer_class(self.get_queryset(pk),data= request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            return Response('errors',status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request ):
        task = self.get_queryset()
        
        if task:
            task.state = False
            task.save()
            return Response({'message':'task deleted'},status= status.HTTP_200_OK)
        return Response({'error':'Not exist'},status= status.HTTP_404_NOT_FOUND)
    
    
class StatusLisCreateApiView(generics.ListCreateAPIView):
    serializer_class=StatusSerializerModel
    queryset= Status.objects.all()