from _json import make_encoder
from builtins import str

from django.db import models

# Create your models here.
#-----------CLASES DE AREAS-----------------
from django.db.models import Model
from django.db.models.fields import return_None


class Area(models.Model):
    Nombre=models.CharField(max_length=50)
    Abreviatura=models.CharField(max_length=5)

    #ver desde otro formulario con NOMBRE
    def __str__(self):
        cadena="{0} => {1}"
        return cadena.format(self.Nombre,self.Abreviatura)

#-----------CLASE DE REGISTRO DE RESERVA----

class Asignar_Horarios_para_Reserva(models.Model):
    área=models.ForeignKey(Area,null=True,on_delete='do_nothing')
    Nombre=models.CharField(max_length=50)
    Sector= models.CharField(max_length=50)
    Tiempo_Uso=models.DateTimeField(blank=True,null=True)
    Imagen=models.ImageField(upload_to='Imagenes',null=True)
    Descripcion=models.TextField(null=True)
    Estado=models.BooleanField(default=True)

    # LISTAR "FK" CON SU NOMBRE
    def __str__(self):
        return str(self.área)



