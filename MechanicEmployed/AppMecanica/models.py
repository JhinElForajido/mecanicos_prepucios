from django.db import models

# Create your models here.

class Mecanico(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    telefono= models.CharField(max_length=12)
class Vehiculo(models.Model):
    patente = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    tipo_vehiculo = models.CharField(max_length=10)

class Usuario(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    edad = models.CharField(max_length=10)
    correo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=12)

class Taller(models.Model):
    nombre = models.CharField(max_length=10)
    tipo = models.CharField(max_length=30)



