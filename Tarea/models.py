from django.db import models

class Tarea(models.Model):
    Tarea = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Tarea}"