from django.contrib import admin

from apps.Gestionar_Areas_Comunes.models import Area,Asignar_Horarios_para_Reserva
# Register your models here.

#-------LISTAR LA TABLA AREA---------------
class AreaAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Abreviatura')
admin.site.register(Area,AreaAdmin)

#-------LISTAR LA TABLA AREAS--------------
class AsignarAdmin(admin.ModelAdmin):
    list_display = ('área','Nombre','Sector','Tiempo_Uso')
admin.site.register(Asignar_Horarios_para_Reserva,AsignarAdmin)




