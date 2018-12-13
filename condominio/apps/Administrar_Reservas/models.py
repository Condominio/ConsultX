from django.db import models

# Create your models here.
from apps.Administrar_Visitas.models import Propietario
from apps.Gestionar_Areas_Comunes.models import Area,Asignar_Horarios_para_Reserva


class Reserva(models.Model):
    propietario=models.ForeignKey(Propietario,on_delete=models.CASCADE)
    Áreas_Disponibles=models.ForeignKey(Asignar_Horarios_para_Reserva,on_delete=models.CASCADE)
    Fecha_Reserva=models.DateTimeField(blank=True,null=True,auto_now=True)

    def __str__(self):
        return str(self.propietario)

    def __str__(self):
        return str(self.Áreas_Disponibles)