from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.

# class Post(models.Model):
#     sno = models.AutoField(primary_key=True)
#     title = models.CharField(max_length=255)
#     description = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='images')
#     timestamp = models.DateTimeField( blank=True)

#     def __str__(self):
#         return self.title + " - " + self.description
    

class Post(models.Model):
    sno= models.AutoField(primary_key=True)
    # comment=models.TextField()
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    # image = models.ImageField(upload_to='static/images')
    user=models.ForeignKey(User, on_delete=models.PROTECT)
    # post=models.ForeignKey(Post, on_delete=models.CASCADE)
    # parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now)
    is_deleted = models.BooleanField(default=False)
