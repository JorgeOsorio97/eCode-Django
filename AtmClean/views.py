from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from ticketFinder.utils import render_to_pdf 
from atmPostService.models import Transaccion

class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        transaccion = Transaccion.objects.filter(id_transaccion = request.GET.get('id_transaccion')).first()
        template = get_template('pdf.html')
        context = {
            "id_atm": transaccion.id_atm.id_atm,
            "folio": transaccion.folio,
            "tipo": definir_tipo(transaccion.tipo),
            "importe": transaccion.importe,
            "cuenta": str(transaccion.cuenta)[-4:],
            "fecha": transaccion.fecha,
            "banco": transaccion.banco,
            "id_transaccion": transaccion.id_transaccion
        } 
        html = template.render(context) 
        pdf = render_to_pdf('pdf.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "pdf%s.pdf" %("12341231")
            content = "inline; filename='%s'" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" %(filename)
            response['Content-Disposition'] = content
            return response

def definir_tipo(tipo):
    if tipo == 0:
        tipo = 'Deposito'
    elif tipo == 1:
        tipo = 'Pago de servicios'
    elif tipo == 2:
        tipo == 'Pago a TC'
    elif tipo == 3:
        tipo = 'Pago de Credito o de Prestamos'
    elif tipo == 4:
        tipo = 'Prestamo Disponible'
    elif tipo == 5:
       tipo = 'Consultar Saldo'
    elif tipo == 6:
        tipo = 'Tiempo aire'
    elif tipo == 7:
        tipo = 'Retiro' 
    return tipo