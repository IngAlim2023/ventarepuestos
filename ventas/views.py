from django.shortcuts import render, redirect

#Vistas basadas en clases:
from django.views.generic.base import TemplateView
from .models import Clientes
# Formulario de clientes
from .forms import AddClienteForm
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

def edit_cliente_view(request):
    return redirect('clientes')

def delete_cliente_view(request):
    return redirect('clientes')

# Table with DataTables

def list_clientes(request):
    clientes = list(Clientes.objects.values())
    data = {'clientes': clientes}
    return JsonResponse(data)

    