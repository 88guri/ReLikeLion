from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def get_by_natural_key(self, id):
        return self.get(id=id)
    
class CustomUser(AbstractUser):
    id = models.CharField(max_length=15, unique=True)
    list_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    major = models.CharField(max_length=20)
    nickname = models.CharField(max_length=10)
    password = models.CharField(max_length=15)
    phone_number = models.CharField(max_length=13)
    introduction = models.CharField(max_length=100)  
    hobby = models.CharField(max_length=50)  
    favorite_food = models.CharField(max_length=50)  

    def save(self, *args, **kwargs):
        
        self.username = self.id
        
        super().save(*args, **kwargs)