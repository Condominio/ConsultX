from _json import make_encoder
from builtins import str

from django.db import models

# Create your models here.
#-----------CLASES DE AREAS-----------------
from django.db.models import Model
from django.db.models.fields import return_None
from django.utils.html import format_html
from django.utils.safestring import mark_safe


#----------CLASE SUB-AREA-------------------
class SubArea(models.Model):
    Nombre=models.CharField(max_length=50)
    Nro_SubÁrea=models.CharField(max_length=5)

    #ver desde otro formulario con NOMBRE
    def __str__(self):
        cadena="{0} - {1}"
        return cadena.format(self.Nro_SubÁrea,self.Nombre)

#----------CLASE AREA-------------------
class Area(models.Model):
    Nombre=models.CharField(max_length=50)
    sub_area=models.ForeignKey(SubArea,on_delete='do_nothing')

    #ver desde otro formulario con NOMBRE
    def __str__(self):
        cadena="{0}  =>  {1}"
        return cadena.format(self.Nombre,self.sub_area)

    # LISTAR "FK" CON SU NOMBRE
    #def __str__(self):
    #    return str(self.sub_area)



#-----------CLASE DE REGISTRO DE RESERVA----

class Asignar_Horarios_para_Reserva(models.Model):
    area=models.ForeignKey(Area,null=True,on_delete='do_nothing')
    Tiempo_Inicio = models.DateTimeField(blank=True, null=True)
    Tiempo_Fin=models.DateTimeField(blank=True,null=True)
    Imagen=models.ImageField(upload_to='Imagenes',null=True)
    Para_Reservar=models.BooleanField(default=True)
    En_Mantenimiento = models.BooleanField(default=True)

    #def __str__(self):
    #    cadena="{0}"
    #    return cadena.format(self.area)

    #ES PARA OBTENER LAS IMAGENES
    def Imagenes(self):
        return format_html("<image src='{}' width='80' height='80' />".format(self.Imagen.url))
    Imagenes.short_description = 'Imagenes'

    # LISTAR "FK" CON SU NOMBRE
    def __str__(self):
        return str(self.area)



