from django.db import models
from Empleado.models import Empleado

class Agenda(models.Model):
    Empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE,to_field='id',db_column='idEmpleado')
    
    def __str__(self):
        return f"{self.pk} : {self.Empleado}"
