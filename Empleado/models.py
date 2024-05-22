from django.db import models
from Rol.views import Rol

class Empleado(models.Model):
    Foto = models.ImageField(upload_to='construred/empleados/', blank=True)
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    DNI = models.CharField(max_length=20, unique=True)
    FechaContratacion = models.DateField()
    Telefono = models.CharField(max_length=20)
    Correo = models.EmailField(max_length=50,unique=True)
    Contraseña = models.CharField(max_length=128)
    Rol = models.ForeignKey(Rol, on_delete=models.CASCADE,to_field='id',db_column='idRol')

    def __str__(self):
        return f"{self.Nombres} {self.Apellidos} DNI:{self.DNI}"
    