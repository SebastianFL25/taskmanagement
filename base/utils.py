from rest_framework import parsers, renderers
from rest_framework.authtoken.models import Token
from rest_framework.compat import coreapi, coreschema
from rest_framework.response import Response
from rest_framework.schemas import ManualSchema
from rest_framework.schemas import coreapi as coreapi_schema
from rest_framework.views import APIView
from .api.serializer import CustomAuthTokenSerializer

from datetime import timedelta
from django.utils import timezone
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from apitaskm.settings.base import TOKEN_EXPIRED_AFTER_SECONDS

class ExpiringTokenAuthentication(TokenAuthentication):
    
    def expires_in(self,token):
        time_elapse = timezone.now() - token.created
        left_time= timedelta(seconds=TOKEN_EXPIRED_AFTER_SECONDS) - time_elapse
        return left_time
    
    def is_token_expired(self,token):
        return self.expires_in(token) < timedelta(seconds=0)
    
    def token_expire_handler(self,token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            print('token expirado')
        return is_expire
        
    def authenticate_credentials(self, key):
        try:
            token=self.get_model().objects.select_related('user').get('key')
            
        except:
            raise AuthenticationFailed('token invalid')
        
        if not token.user.is_active:
            raise AuthenticationFailed('inactive or deleted user')
        
        is_expire =self.token_expire_handler
        if is_expire:
            raise AuthenticationFailed('Token expired')
        return (token.user,token)



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
