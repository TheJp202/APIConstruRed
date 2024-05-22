from django.db import models
from Equipo.models import Equipo
from Proyecto.models import Proyecto
class EquipoProyecto(models.Model):
    Equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE,to_field='id',db_column='idEquipo')
    Proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE,to_field='id',db_column='idProyecto')

    def __str__(self):
        return f"Equipo:{self.Equipo} Proyecto:{self.Proyecto}"