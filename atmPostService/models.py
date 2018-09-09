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
    id_transaccion = models.CharField(max_length=50, primary_key = True)

    def save(self, *args, **kwargs):
        self.id_transaccion = str(self.id_atm.id_atm) + str(self.tipo) + str(self.folio) + str(self.fecha.year) + str(self.fecha.month)+ str(self.fecha.day)+str(self.fecha.hour)+str(self.fecha.minute)+str(self.fecha.second)
        super(Transaccion, self).save(*args, **kwargs)
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
    id_transaccion = models.CharField(max_length = 50, null = True)
    fecha_uso = models.DateTimeField(null = True, auto_now = True)
    id_trans = models.CharField(max_length = 50, null = True)

