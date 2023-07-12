from rest_framework import serializers
from base.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass


class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model=User
        fields= ('email','password')
        
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'], 
            validated_data['password']
        )
        return user

class UserTokenSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model=User
        fields= (
            
            'email',
            'password',
            )
        