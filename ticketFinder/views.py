from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import pandas as pd


# Create your views here.
def index(request):
    return render(request, 'index.html')

def options(request):
    return render(request, 'options.html')

def ecode(request):
    return render(request, 'eCode.html')

def cuestionario(request):
    return render(request, 'cuestionario.html')

@csrf_exempt
def POST_cuestionario(request):
    tipo = request.POST.get('tipo', None)
    fecha = request.POST.get('fecha', None)
    hora = request.POST.get('hora', None)
    estado = request.POST.gtet('estado', None)
    municipio = request.POST.get('municipio', None)
    ultimos_digitos = request.POST.get('u4', None)
    banco = request.POST.get('banco', None)

    df = pd.DataFrame(list(Transaccion.objects.filter(tipo = tipo).values()))
    print(df)
    response = {'succes': True, 'beneficiario': cuenta.beneficiario}
    return JsonResponse(response)