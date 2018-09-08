from django.db import models

# Create your models here.
class Transaccion(models.Model):
    folio = models.BigIntegerField()
    id_atm = models.ForeignKey('Cajero', on_delete = models.CASCADE)
    tipo = models.CharField(max_length =10)
    importe = models.FloatField()
    cuenta = models.ForeignKey('Cuenta', on_delete = models.CASCADE)
    fecha = models.DateTimeField()
    banco = models.CharField(max_length = 100)
#    no_tarjeta = models.BigIntegerField()

class Cajero(models.Model):
    id_atm = models.CharField(max_length=10, primary_key = True)
    estado = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)

class Cuenta(models.Model):
      no_cuenta = models.BigIntegerField(primary_key = True)
      beneficiario = models.CharField(max_length=50)
      saldo = models.FloatField()
