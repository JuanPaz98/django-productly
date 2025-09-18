from django.shortcuts import render
from django.http import HttpResponse
from .models import Producto

# Create your views here.


def index(request):
    productos = Producto.objects.all()
    nombres = [producto.nombre for producto in productos]  # list comprehension
    return HttpResponse(", ".join(nombres))
