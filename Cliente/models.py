from django.db import models

class Cliente(models.Model):
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    DNI = models.CharField(max_length=20, unique=True)
    Telefono = models.CharField(max_length=20)
    Correo = models.EmailField(max_length=50,unique=True)
    Contraseña = models.CharField(max_length=128)
    def __str__(self):
        return f"{self.Nombres} {self.Apellidos} DNI:{self.DNI}"
    