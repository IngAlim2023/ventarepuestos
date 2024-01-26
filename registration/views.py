#Vistas basadas en clases:
from django.views.generic.base import TemplateView
# Vista clientes
from .models import User


# Create your views here.
class Clientes(TemplateView):
    template_name = 'registration/clientes.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        usuarios = User.objects.all()  # Trae todos los usuarios
        
        context.update({
            "usuarios": usuarios,
        })
        return context