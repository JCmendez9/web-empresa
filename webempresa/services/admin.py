from django.contrib import admin
from .models import Service

# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')  # Para que no se pueda editar en el admin

admin.site.register(Service, ServiceAdmin)