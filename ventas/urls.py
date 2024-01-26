from django.urls import path
from ventas.views import *
from . import views 


urlpatterns = [
    path('', Ventas.as_view(), name= 'ventas'),
    path('calculadora/', Calculadora.as_view(), name= 'calculadora'),
    path('Clientes/', ClientesView.as_view(), name= 'clientes'),
    path('Addcliente/', views.add_cliente_view, name='addcliente'),
    path('Editcliente/', views.edit_cliente_view, name='editcliente'),
    path('Deletecliente/', views.delete_cliente_view, name='deletecliente'),
    #Datable
    path('list_clientes/', views.list_clientes, name='list_clientes'),
]