from django.urls import path
from ventas.views import *
from . import views 


urlpatterns = [
    path('', IndexPageView.as_view(), name= 'inicio'),
    path('calculadora/', Calculadora.as_view(), name= 'calculadora'),
]