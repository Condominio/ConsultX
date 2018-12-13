#from django.contrib.gis.gdal.prototypes.raster import auto_create_warped_vrt
from builtins import set

from django.db import models


# Create your models here.

#-------------------------Clase propietario------------------------

class Propietario(models.Model):
    Nro_Habitacion = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)



    def Lista(self):
        cadena = "{0} - {1} {2}"
        return cadena.format(self.Nro_Habitacion, self.Nombre, self.Apellido)

    def __str__(self):
        return self.Lista()

#-------------------------Clase propietario------------------------
class Visitante(models.Model):
    C_I = models.CharField(max_length=8)
    Nombre=models.CharField(max_length=100)
    Apellido = models.CharField(max_length=100)


    def lista(self):
        cadena="{0} - {1} {2}"
        return cadena.format(self.C_I,self.Nombre,self.Apellido)

    def __str__(self):
        return self.lista()

#---------------------------------clase visita---------------------#

class Visita(models.Model):
    visitante=models.ForeignKey(Visitante,on_delete='do_nothing')
    propietario=models.ForeignKey(Propietario,on_delete='do_nothing')
    Hora_Entrada=models.DateTimeField(blank=True,null=True,auto_now=True)
    Hora_Salida=models.DateTimeField(blank=True,null=True)
    t_a=(('C','A_pie'),('A','Automovil'))
    Tipo_Acceso=models.CharField(max_length=1,choices=t_a,default='C')
    Descripcion=models.TextField()

    #  VISTA DE LA LLAVE FORANEA
    def __str__(self):
        return str(self.visitante)

    #  VISTA DE LA LLAVE FORANEA
    def  __str__(self):
        return str(self.propietario)









