
from rest_framework import serializers
from base.models import User
from django.contrib.auth import authenticate        
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class UserUpdateSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model=User
        fields=['email']
    
class PaswordSerializer(serializers.Serializer):
    password= serializers.CharField(max_length=130,min_length=6,write_only=True)
    password2= serializers.CharField(max_length=130,min_length=6,write_only=True)
    
    def validate(self, data):
        password = data.get("password")
        password2 = data.get("password2")

        if password != password2:
            raise serializers.ValidationError("Las contraseñas no coinciden.")

        return data

        
class UserSerializers(serializers.ModelSerializer):
    email = serializers.EmailField()
    
    class Meta:
        model=User
        fields= ('id','email','password')
        
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['email'], 
            validated_data['password']
        )
        return user
    
class UserRDSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields= ('id','email','password')
    



class AuthTokenSerializerp(serializers.Serializer):
    email = serializers.EmailField(
        label=("email"),
        write_only=True
    )
    password = serializers.CharField(
        label=("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=("Token"),
        read_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = ('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
       
class CustomAuthTokenSerializer(AuthTokenSerializerp):
    email = serializers.EmailField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            # Try to authenticate the user
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            # If authentication fails, raise an error
            if not user:
                msg = ('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')

        else:
            msg = ('Must include "email" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
    
        

