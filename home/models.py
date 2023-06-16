from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)


    def __str__(self):
        return self.name + " - " + self.email
    
# class User(AbstractUser):
#     username = models.EmailField(unique=True)
    #phone_number = models.CharField(max_length=10, unique=True)

