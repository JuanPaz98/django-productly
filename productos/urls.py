from django.urls import path
from . import views

# app_name = "productos"

urlpatterns = [
    path('', views.index, name='index'),
    path('nuevo', views.formulario, name='nuevo_producto'),
    path('<int:producto_id>', views.detalle, name='producto_detalle'),
]
