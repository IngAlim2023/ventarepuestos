from django.db import models

# Create your models here.

# # funcion para la carga de imagenes de usuario:
def upload_image(instance, filename):
    return "img/producto/{id}/{filename}".format( id = instance.pk, filename = filename)

class Producto(models.Model):
    descripcion = models.CharField(max_length=80, unique= True, null= True)
    imagen = models.ImageField(upload_to='productos', null= True, blank=True)
    costo = models.DecimalField(max_digits=15, decimal_places=1, null=False)
    ubicacion = models.DecimalField(max_digits=5, decimal_places=1, null=False)
    cantidad = models.DecimalField(max_digits=15, decimal_places=1, null=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        order_with_respect_to = 'descripcion'

    def __str__(self):
        return self.descripcion
    
class TipoDocumentoCliente(models.Model):
    tipo_documento = models.CharField('Tipo de documento', max_length=30)
    created = models.DateField(auto_now_add=True)
    update = models.DateField(auto_now=True)

    class Meta:
        verbose_name = 'Tipo de documento'
        verbose_name_plural = 'Tipos de documentos'
    
    def __str__(self):
        return f'{self.tipo_documento}'

# Create your models here.
class Clientes(models.Model):

    # Sobreescribo el campo'username':
    nombre = models.CharField(verbose_name='Nombre', max_length=20)
    apellido = models.CharField(verbose_name='Apellido', max_length=20)
    tipo_id = models.ForeignKey(TipoDocumentoCliente, on_delete=models.DO_NOTHING, null=True)
    identification = models.CharField(verbose_name='Número de Identificación', max_length = 20 , unique= True)
    address = models.CharField(verbose_name= 'Dirección', max_length=255)
    phone = models.CharField(verbose_name= 'Telefono', max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
        order_with_respect_to = 'nombre'

    def __str__(self):
        return self.nombre