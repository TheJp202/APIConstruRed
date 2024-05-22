from django.db import models
from TipoMensaje.models import TipoMensaje
from Cliente.models import Cliente

class Mensaje(models.Model):
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, to_field='id',db_column='idCliente')
    TipoMensaje = models.ForeignKey(TipoMensaje, on_delete=models.CASCADE,to_field='id',db_column='idTipoMensaje')
    Descripcion = models.TextField()
    Estado = models.CharField(max_length=100,default="Pendiente")
    FechaHoraMensaje = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Cli:{self.Cliente}-TipMen:{self.TipoMensaje}-Fecha/Hora:{self.FechaHoraMensaje}"
