from .serializer import UserSerializers
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken

class CreateGenericView(CreateAPIView):
    serializer_class = UserSerializers
    
    def post(self,request):
        serializers = self.serializer_class(data = request.data)
        
        if serializers.is_valid():
            serializers.save()
            return Response({'message':'User created successfully'},status= status.HTTP_201_CREATED)
        return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)
