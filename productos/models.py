from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=255, default="")

    def __str__(self):
        return str(self.nombre) if self.nombre else ""


class Producto(models.Model):
    nombre = models.CharField(max_length=255, default="")
    stock = models.IntegerField()
    puntaje = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.nombre) if self.nombre else ""
