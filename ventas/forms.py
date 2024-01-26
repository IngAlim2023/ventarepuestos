from django import forms
from ventas.models import Clientes

class AddClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
                'nombre', 
                'apellido',
                'tipo_id',
                'identification',
                'address',
                'phone',
            ]
        labels = {
            'nombre':'Nombre', 
            'apellido':'Apellido',
            'tipo_id':'Tipo de documento',
            'identification':'Identificación',
            'address':'Dirección',
            'phone':'Teléfono',
        }
        widgets = {
            'nombre':  forms.TextInput(attrs={'class': 'form-control'}),
            'apellido':  forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_id':  forms.Select(attrs={'class': 'form-select'}),
            'identification':  forms.TextInput(attrs={'class': 'form-control'}),
            'address':  forms.TextInput(attrs={'class': 'form-control'}),
            'phone':  forms.TextInput(attrs={'class': 'form-control'}),
            
        }