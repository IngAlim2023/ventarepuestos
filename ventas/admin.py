from django.contrib import admin
from ventas.models import Producto, Clientes, TipoDocumentoCliente, Egreso, ProductosEgreso

# Register your models here.

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('descripcion', 'imagen', 'ubicacion', 'costo', 'cantidad','created', 'modified')
    search_fields = ['descripcion', 'ubicacion']
    readonly_fields = ('created', 'modified')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class ClientesAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'tipo_id', 'identification', 'address', 'phone','created', 'modified')
    search_fields = ['nombre', 'apellido', 'identification']
    readonly_fields = ('created', 'modified')
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Producto, ProductoAdmin)
admin.site.register(TipoDocumentoCliente)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Egreso)
admin.site.register(ProductosEgreso)