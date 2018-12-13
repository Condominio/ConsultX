from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.Gestionar_Areas_Comunes.models import Area,Asignar_Horarios_para_Reserva,SubArea
# Register your models here.

#-------LISTAR LA TABLA SUB-AREA---------------
class SubAreAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Nro_SubÁrea')
admin.site.register(SubArea,SubAreAdmin)

#-------LISTAR LA TABLA AREA---------------
class AreAdmin(admin.ModelAdmin):
    list_display = ('Nombre','sub_area')
admin.site.register(Area,AreAdmin)


#-------LISTAR LA TABLA AREAS--------------
class AsignarAdmin(admin.ModelAdmin):
    list_display = ('area','Tiempo_Inicio','Tiempo_Fin','Imagenes')
admin.site.register(Asignar_Horarios_para_Reserva,AsignarAdmin)






