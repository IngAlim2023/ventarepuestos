from django import forms
from ventas.models import Clientes, Producto

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

# Productos
        
class AddProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = [
                'descripcion', 
                'imagen',
                'costo',
                'ubicacion',
                'cantidad',
            ]
        labels = {
            'descripcion':'Descripción', 
            'imagen':'Imagen',
            'costo':'Costo',
            'ubicacion':'Ubicación',
            'cantidad':'Cantidad',
        }
        widgets = {
            'descripcion':  forms.TextInput(attrs={'class': 'form-control'}),
            'imagen':  forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'costo':  forms.NumberInput(attrs={'class': 'form-select'}),
            'ubicacion':  forms.NumberInput(attrs={'class': 'form-control'}),
            'cantidad':  forms.NumberInput(attrs={'class': 'form-control'}),            
        }