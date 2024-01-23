from django.shortcuts import render

#Vistas basadas en clases:
from django.views.generic.base import TemplateView

# Create your views here.

class IndexPageView(TemplateView):
    #Indicar que template usa esta vista
    template_name = 'core/index.html'

class Calculadora(TemplateView):
    #Indicar que template usa esta vista
    template_name = 'core/calculadora.html'