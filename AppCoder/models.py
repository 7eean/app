from django.db import models

# Create your models here.

class Series (models.Model):

    nombre=models.CharField(max_length=40)
    reseña=models.TextField(max_length=240)
    imagen=models.ImageField(upload_to = 'resenias', null=True)