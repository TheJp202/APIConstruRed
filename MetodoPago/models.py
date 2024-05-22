from django.db import models

class MetodoPago(models.Model):
    Metodo = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.Metodo}"