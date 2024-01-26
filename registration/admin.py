from django.contrib import admin
from registration.models import *
# Register your models here.

class ClientesAdmin(admin.ModelAdmin):
    search_fields = ['nombre']
    readonly_fields = {'created', 'modified'}
    filter_horizontal ={}
    list_filter = {}
    fieldsets = {}

admin.site.register(User)
admin.site.register(TipoDocumento)