from django.db import models

# Create your models here.


class Categoria(models.Model):
    id = models.IntegerField()
    nombre = models.CharField(max_length=255),


class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    stock = models.IntegerField()
    puntaje = models.FloatField()
    Categoria = models.ForeignKey(Categoria.id, on_delete=models.CASCADE)
