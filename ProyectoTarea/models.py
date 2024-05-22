from django.db import models
from Proyecto.models import Proyecto
from Tarea.models import Tarea


class ProyectoTarea(models.Model):
    Proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE,to_field='id',db_column='idProyecto')
    Tarea = models.ForeignKey(Tarea,on_delete=models.CASCADE,to_field='id',db_column='idTarea')
    Estado = models.CharField(max_length=50,default="Pendiente")
    FechaInicio = models.DateField()
    FechaFinal = models.DateField()
    def __str__(self):
        return f"Proyecto: {self.Proyecto}-Tarea:{self.Tarea}"
    
    