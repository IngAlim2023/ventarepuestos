from django.shortcuts import render, redirect

#Vistas basadas en clases:
from django.views.generic.base import TemplateView
from .models import Clientes, Producto
# Formulario de clientes y producto
from .forms import AddClienteForm, AddProductoForm
#messages
from django.contrib import messages

#Table Datatable
from django.http.response import JsonResponse

# Create your views here.

class Ventas(TemplateView):
    #Indicar que template usa esta vista
    template_name = 'core/ventas.html'

class Calculadora(TemplateView):
    #Indicar que template usa esta vista
    template_name = 'core/calculadora.html'

# Create your views here.
class ClientesView(TemplateView):
    template_name = 'core/clientesv.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        clientes = Clientes.objects.all()  # Trae todos los usuarios
        form = AddClienteForm()
        context.update({
            "clientes": clientes,
            'form': form,
        })
        return context
    
def add_cliente_view(request):
    if request.POST:
        form = AddClienteForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request, "Error al guardar el cliente")
                return redirect('clientes')
    return redirect('clientes')


def delete_cliente_view(request, clientes_id):
    clientes = Clientes.objects.filter(id= clientes_id)
    clientes.delete()
    return redirect('clientes')

# Table with DataTables

def list_clientes(request):
    clientes = list(Clientes.objects.values())
    data = {'clientes': clientes}
    return JsonResponse(data)

# Productos

class ProductosView(TemplateView):
    template_name = 'core/productos.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        productos = Producto.objects.all()  # Trae todos los usuarios
        form = AddProductoForm()
        context.update({
            "productos": productos,
            'form': form,
        })
        return context

def add_producto_view(request):
    if request.POST:
        form = AddProductoForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save()
            except:
                messages(request, "Error al guardar el producto")
                return redirect('productos')
    return redirect('productos')

# Table with DataTables

def list_productos(request):
    productos = list(Producto.objects.values())
    data = {'productos': productos}
    return JsonResponse(data)