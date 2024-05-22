from django.db import models
from MetodoPago.models import MetodoPago
from Contrato.models import Contrato
from Cliente.models import Cliente

class Factura(models.Model):
    Contrato = models.ForeignKey(Contrato,on_delete=models.CASCADE,to_field='id',db_column='idContrato')
    MetodoPago = models.ForeignKey(MetodoPago,on_delete=models.CASCADE,to_field='id',db_column='idMetodoPago')
    Cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE,to_field='id',db_column='idCliente')
    MontoCliente = models.DecimalField(max_digits=9,decimal_places=2)
    FechaPago = models.DateField()
    Factura = models.FileField(upload_to='construred/factura/')
    
    def __str__(self):
        return f"Cont: {self.Contrato}-Cli: {self.Cliente}-Fecha: {self.FechaPago}"
    
    