from django.db import models

# Create your models here.
class Transaccion(models.Model):
    folio = models.BigIntegerField()
    id_atm = models.ForeignKey('Cajero', on_delete = models.CASCADE)
    tipo = models.IntegerField()
    importe = models.FloatField()
    cuenta = models.CharField(max_length=50)
    fecha = models.DateTimeField()
    banco = models.CharField(max_length = 100)
    id_transaccion = models.CharField(max_length=50, null = True)

    def save(self, *args, **kwargs):
        self.id_transaccion = str(self.id_atm) + str(self.tipo) + str(self.folio)
#    no_tarjeta = models.BigIntegerField()

    def __str__(self):
        return self.id_transaccion

class Cajero(models.Model):
    id_atm = models.CharField(max_length=10, primary_key = True)
    estado = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=50)
    localidad = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=50, null = True)

class Cuenta(models.Model):
    no_cuenta = models.BigIntegerField(primary_key = True)
    beneficiario = models.CharField(max_length=50)
    saldo = models.FloatField()

class eCode(models.Model):
    ecode = models.CharField(max_length=5)
    id_transaccion = models.ForeignKey('Transaccion', on_delete= models.CASCADE, null = True)
    fecha_uso = models.DateTimeField(null = True)

