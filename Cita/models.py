from django.db import models
from Empleado.models import Empleado
from Cliente.models import Cliente

class Cita(models.Model):
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE,to_field='id',db_column='idEmpleado')
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, to_field='id',db_column='idCliente')
    FechaHora = models.DateTimeField()
    Motivo = models.TextField()
    
    def __str__(self):
        return f"Emp:{self.Empleado}-Cli:{self.Cliente}-Fecha/Hora:{self.FechaHora}"
