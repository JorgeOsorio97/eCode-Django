from django.contrib import admin
from atmPostService.models import Transaccion, Cuenta, Cajero, eCode
# Register your models here.

admin.site.register(Transaccion)
admin.site.register(Cuenta)
admin.site.register(Cajero)
admin.site.register(eCode)