from django.db import models

# Create your models here.

class MyFamily(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fechaCumple = models.DateField()