#django
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):
    
    def create_user(self,email, password=None, **extra_fields):
        """Creates and saves a new user with the given email and password."""
        if not email:
            raise ValueError('Email address is required.')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save()#using=self._db
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Creates and saves a new superuser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)