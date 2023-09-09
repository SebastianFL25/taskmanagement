from datetime import timedelta
from django.utils import timezone

from rest_framework.authentication import TokenAuthentication

from apitaskm.settings.base import TOKEN_EXPIRED_AFTER_SECONDS

class ExpiringTokenAuthentication(TokenAuthentication):
    expired= False
    
    def expires_in(self,token):
        time_elapse = timezone.now() - token.created
        left_time= timedelta(seconds=TOKEN_EXPIRED_AFTER_SECONDS) - time_elapse
        return left_time
    
    def is_token_expired(self,token):
        return self.expires_in(token) < timedelta(seconds=0)
    
    def token_expire_handler(self,token):
        is_expire = self.is_token_expired(token)
        if is_expire:
            self.expired=True
            user = token.user
            token.delete()
            token=self.get_model().objects.create(user=user)
            
        return is_expire,token
        
    def authenticate_credentials(self, key):
        user,token,message=None,None,None
        try:
            token=self.get_model().objects.select_related('user').get(key=key)
            user=token.user
        except self.get_model().DoesNotExist:
            message= "token invalid"
            self.expired=True
            
        if token is not None:
            if not token.user.is_active:
                message= "inactive or deleted user"
        
            is_expire =self.token_expire_handler(token)
            if is_expire:
                message= "Token expired"
            
        return (user,token,message,self.expired)



