from django.urls import path
from ventas.views import *
from . import views 


urlpatterns = [
    path('', Ventas.as_view(), name= 'ventas'),
    path('calculadora/', Calculadora.as_view(), name= 'calculadora'),
    path('Clientes/', ClientesView.as_view(), name= 'clientes'),
    path('Addcliente/', views.add_cliente_view, name='addcliente'),
    path('Deletecliente/<int:clientes_id>', views.delete_cliente_view, name='deletecliente'),
    #Datable
    path('list_clientes/', views.list_clientes, name='list_clientes'),
    #productos
    path('Productos/', ProductosView.as_view(), name= 'productos'),
    path('Addproducto/', views.add_producto_view, name='addproducto'),
    #Datable
    path('list_productos/', views.list_productos, name='list_productos'),
    #Añadir ventas
    #path('Add_ventas/', views.add_ventas, name = 'addventa'),
    #path('Export/', views.export_pdf, name = 'exportpdf'),
   # path('Export/<id>/<iva>', views.export_pdf, name = 'exportpdf'),    
    
]