from django.db import models

# Create your models here.

class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    timestamp = models.DateTimeField( blank=True)

    def __str__(self):
        return self.title + " - " + self.description
