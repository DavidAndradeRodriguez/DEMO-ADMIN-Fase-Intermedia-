from django.db import models

# Create your models here.
class Tecnologia(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    stock = models.PositiveSmallIntegerField()
    fecha_ingreso = models.DateField()
    descripcion = models.TextField()

    def __str__(self) -> str:
        return self.nombre

class Limpieza(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    stock = models.PositiveSmallIntegerField()
    fecha_ingreso = models.DateField()
    descripcion = models.TextField()

    def __str__(self) -> str:
        return self.nombre
    
class Comida(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    stock = models.PositiveSmallIntegerField()
    fecha_ingreso = models.DateField()
    descripcion = models.TextField()

    def __str__(self) -> str:
        return self.nombre
    
class Ropa(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.PositiveIntegerField()
    stock = models.PositiveSmallIntegerField()
    fecha_ingreso = models.DateField()
    descripcion = models.TextField()

    def __str__(self) -> str:
        return self.nombre