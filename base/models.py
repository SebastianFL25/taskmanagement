
#django
from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import CustomUserManager
    
class User(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(max_length = 250, unique = True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.email}'
