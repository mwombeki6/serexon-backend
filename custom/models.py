from django.db import models
from django.contrib.auth.models import AbstractUser

from .manager import UserManager

class User(AbstractUser):
    """Custom User  Model
    """
    
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    is_customer = models.BooleanField(default=False)
    is_vendor = models.BooleanField(default=False)
    
    objects = UserManager()