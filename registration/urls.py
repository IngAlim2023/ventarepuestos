from django.urls import path
from registration.views import *
from . import views 


urlpatterns = [
    #path('', Ventas.as_view(), name= 'ventas'),
    path('Usuarios/', Clientes.as_view(), name= 'usuarios'),
]