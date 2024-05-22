from django.db import models
from Proyecto.models import Proyecto

class Archivo(models.Model):
    Nombre = models.CharField(max_length=100)
    Archivo = models.FileField(upload_to='construred/archivos/')
    Proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE,to_field='id',db_column='idProyecto')
    
    def __str__(self):
        return f"{self.Nombre}"
    
    