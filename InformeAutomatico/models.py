from django.db import models
from TipoInforme.models import TipoInforme

class InformeAutomatico(models.Model):
    TipoInforme = models.ForeignKey(TipoInforme,on_delete=models.CASCADE,to_field='id',db_column='idTipoInforme')
    Nombre = models.CharField(max_length=100)
    Archivo = models.FileField(upload_to='construred/informes/')
    
    def __str__(self):
        return f"{self.Nombre}"
    
    