from django.db import models

class TipoInforme(models.Model):
    Nombre = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Nombre}"