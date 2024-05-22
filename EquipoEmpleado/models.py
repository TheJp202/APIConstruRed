from django.db import models
from Equipo.models import Equipo
from Empleado.models import Empleado
class EquipoEmpleado(models.Model):
    Equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE,to_field='id',db_column='idEquipo')
    Empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE,to_field='id',db_column='idEmpleado')

    def __str__(self):
        return f"Equipo:{self.Equipo} Emp:{self.Empleado}"