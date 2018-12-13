from django.contrib import admin

# Register your models here.
from apps.Administrar_Reservas.models import Reserva


class ResAdmin(admin.ModelAdmin):
    list_display = ('propietario','Áreas_Disponibles', 'Fecha_Reserva')
admin.site.register(Reserva,ResAdmin)



