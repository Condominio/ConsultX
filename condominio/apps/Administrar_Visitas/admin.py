from django.contrib import admin

from apps.Administrar_Visitas.models import Propietario,Visitante,Visita


# Register your models here.
# -------PROPIETARIO--------------
class ProAdmin(admin.ModelAdmin):
    list_display = ('Nro_Habitacion', 'Nombre', 'Apellido')
admin.site.register(Propietario, ProAdmin)


# -------VISITANTE------------------
class VisitAdmin(admin.ModelAdmin):
    list_display = ('C_I','Nombre','Apellido')
admin.site.register(Visitante,VisitAdmin)

# -------VISITAS------------------
class VisAdmin(admin.ModelAdmin):
   list_display = ('visitante','propietario','Hora_Entrada','Hora_Salida','Tipo_Acceso')
admin.site.register(Visita,VisAdmin)
