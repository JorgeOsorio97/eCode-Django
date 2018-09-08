from django.shortcuts import render
from django.http import JsonResponse
from atmPostService.models import Cuenta, Cajero, Transaccion, eCode
from datetime import datetime, timedelta


# Create your views here.

def POST_transaccion(request):
    print('entro')
    tipo = request.POST.get('tipo')  
    # if tipo == 0:
    #     tipo = 'deposito'
    # elif tipo == 1:
    #     tipo = 'pago_servicio'
    # elif tipo == 2:
    #     tipo == 'pago_tc'
    # elif tipo == 3:
    #     tipo = 'pago_credito'
    # elif tipo == 4:
    #     tipo = 'prestamo_disponible'
    # elif tipo == 5:
    #     tipo = 'consultar_saldo'
    # elif tipo == 6:
    #     tipo = 'tiempo_aire'
    # elif tipo == 7:
    #     tipo = 'retiro'
    
    id_atm = request.POST.get('id_atm')
    importe = request.POST.get('importe')
    cuenta = request.POST.get('cuenta')
    fecha = request.POST.get('fecha')
    banco = request.POST.get('banco')
    folio = request.POST.get('folio')
    no_tarjeta = request.POST.get('no_tarjeta')
    trans = Transaccion(folio = folio, id_atm = id_atm, 
                        tipo = tipo, importe = importe, 
                        cuenta = cuenta, 
                        fecha = datetime.fromtimestamp(fecha)+timedelta(hours = 5), 
                        banco = 'Santander')
    if request.POST.get('ticket',1) == 1:
        ecode = eCode.objects.filter(fecha_uso__isnull = True).first()
        print(ecode.ecode)
        response = {'succes':True, 'eCode': ecode.ecode}
    else:
        response = {'succes':True}
    return JsonResponse(response)

def POST_deposito(request):
    cuenta = request.POST.get('cuenta')
    # TODO: buscar beneficiario de la cuenta
    response = {'succes': True}
    return JsonResponse(response)