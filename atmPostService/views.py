from django.shortcuts import render
from django.http import JsonResponse
from atmPostService.models import Cuenta, Cajero, Transaccion, eCode
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from atmPostService.poblar_ecode import poblar_transacciones


# Create your views here.
@csrf_exempt
def POST_transaccion(request):
    tipo = request.POST.get('tipo')  
   
    print(request.POST)
    id_atm = Cajero.objects.filter(id_atm=request.POST.get('id_atm')).first()
    importe = request.POST.get('importe')
    cuenta = request.POST.get('cuenta')
    fecha = int(request.POST.get('fecha'))/1000 
    banco = request.POST.get('banco')
    folio = request.POST.get('folio')
    #no_tarjeta = request.POST.get('no_tarjeta')
    trans = Transaccion(folio = folio, id_atm = id_atm, 
                        tipo = tipo, importe = importe, 
                        cuenta = cuenta, 
                        fecha = datetime.fromtimestamp(fecha)-timedelta(hours = 5), 
                        banco = banco)
    trans.save()
    print(trans)
    if request.POST.get('ecode',0) == '1':
        ecode = eCode.objects.filter(id_trans__isnull = True).update(id_trans=trans.id_transaccion, fecha_uso = datetime.now())
        actual_ecode = eCode.objects.filter(id_trans = trans.id_transaccion).first()
        # ecode.id_transaccion = trans
        # ecode.fecha_uso = datetime.now()  
        # ecode.update()
        response = {'succes':True, 'ecode': actual_ecode.ecode, 'id_transaccion': trans.id_transaccion}
    else:
        response = {'succes':True, 'id_transaccion': trans.id_transaccion}
    return JsonResponse(response)

def POST_deposito(request):
    poblar_transacciones()
    response = {'succes': True, 'beneficiario': cuenta.beneficiario}
    return JsonResponse(response)