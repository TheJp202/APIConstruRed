from django.db import models
from Agenda.models import Agenda

class AgendaTarea(models.Model):
    Agenda = models.ForeignKey(Agenda,on_delete=models.CASCADE,to_field='id',db_column='idAgenda')
    Tarea = models.TextField()
    FechaHora = models.DateTimeField()
    Estado = models.CharField(max_length=50,default="Pendiente")
    def __str__(self):
        return f"Agenda: {self.Agenda}-Tarea:{self.Tarea}"
    
    