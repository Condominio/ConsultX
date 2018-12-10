from django.db import models


# Create your models here.

class Propietario(models.Model):
    Nro_Habitacion = models.CharField(max_length=50)
    Nombre = models.CharField(max_length=100)
    Apellido_Materno = models.CharField(max_length=100)
    Apellido_Paterno = models.CharField(max_length=100)


    def Lista(self):
        cadena = "{0} => {1} {2} {3}"
        return cadena.format(self.Nro_Habitacion, self.Nombre, self.Apellido_Materno, self.Apellido_Paterno)


    def __str__(self):
        return self.Lista()
#---------------------------------clase visita---------------------#

class Visita(models.Model):
    CI=models.CharField(max_length=8)
    Nombre=models.CharField(max_length=100)
    Apellido_Materno = models.CharField(max_length=100)
    Apellido_Paterno = models.CharField(max_length=100)
    propietario=models.ForeignKey(Propietario,on_delete='do_nothing')
    Hora_Inicio=models.DateTimeField(blank=True,null=True)
    Hora_Fin=models.DateTimeField(blank=True,null=True)
    t_a=(('C','Caminando'),('A','Automovil'))
    Tipo_Acceso=models.CharField(max_length=1,choices=t_a,default='C')
    Descripcion=models.TextField()

    def ListaVisita(self):
        cadena = "{0} <=> {1} {2} {3}"
        return cadena.format(self.CI,self.Nombre,self.Apellido_Materno,self.Apellido_Paterno)

    def __str__(self):
        return self.ListaVisita()

#---------------------------------clase Reservas---------------------#









