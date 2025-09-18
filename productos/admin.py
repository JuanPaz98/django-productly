from django.contrib import admin
from .models import Categoria, Producto

# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')


class ProductoAdmin(admin.ModelAdmin):
    exclude = ('fecha_creacion', )
    list_display = ('id', 'nombre', 'stock',
                    'puntaje', 'categoria', 'fecha_creacion')


admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Producto, ProductoAdmin)
