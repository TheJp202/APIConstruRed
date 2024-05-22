from django.db import models
from Equipo.models import Equipo

class Reunion(models.Model):
    FechaHoraInicio = models.DateTimeField()
    FechaHoraFinal = models.DateTimeField()
    Motivo = models.TextField()
    Equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE,to_field='id',db_column='idEquipo')    
    def __str__(self):
        return f"Reunión {self.FechaHoraInicio} - {self.FechaHoraFinal}"