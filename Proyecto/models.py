from django.db import models

class Proyecto(models.Model):
    Nombre = models.CharField(max_length=100)
    Imagen = models.ImageField(upload_to='construred/proyectos/')
    Descripcion = models.TextField()
    FechaInicio = models.DateField()
    FechaFinal = models.DateField()
    
    def __str__(self):
        return f"{self.Nombre}"
