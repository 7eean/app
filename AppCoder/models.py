from django.db import models

# Create your models here.

class MyFamily(models.Model):
    nombre = models.CharField(max_length=60)
    edad = models.IntegerField()
    fechaCumple = models.DateField()

class Curso(models.Model):
    nombre = models.CharField(max_length=60)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)

class Entregables(models.Model):
    nombre = models.CharField(max_length=60)
    fechaEntrega = models.DateField()