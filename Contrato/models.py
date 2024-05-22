from django.db import models
from Proyecto.models import Proyecto


class Contrato(models.Model):
    Proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE,to_field='id',db_column='idProyecto')
    Nombre = models.CharField(max_length=100)
    Descripcion = models.TextField()
    PrecioContrato = models.IntegerField()
    Estado = models.CharField(max_length=50,default="Pendiente")
    
    def __str__(self):
        return f"{self.Nombre}"
    
    