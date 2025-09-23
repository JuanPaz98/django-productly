from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from .models import Producto
from .forms import ProductoForm

# Create your views here.


def index(request):
    productos = Producto.objects.all()

    return render(
        request,
        'index.html',
        context={'productos': productos}
    )


def detalle(request, producto_id):
    try:
        producto = Producto.objects.get(id=producto_id)
        return render(
            request,
            'detalle.html',
            context={'producto': producto}
        )
    except Producto.DoesNotExist:
        raise Http404()


def formulario(request):
    try:
        if request.method == 'POST':
            form = ProductoForm(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/productos')
        else:
            form = ProductoForm()

        return render(
            request,
            'formulario-producto.html',
            context={'form': form}
        )
    except Producto.DoesNotExist:
        raise Http404()
