from .serializer import UserSerializers
from rest_framework import generics 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class CreateGenericView(generics.CreateAPIView):
    serializer_class = UserSerializers
    permission_classes= (IsAuthenticated,)
    

    def post(self,request):
        serializers = self.serializer_class(data = request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response({'message':'Usuario creado correctamente'},status= status.HTTP_201_CREATED)
        return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)
