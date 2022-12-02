from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    company = models.CharField(max_length=50)
    nickname = models.CharField(max_length=50)
    
    
