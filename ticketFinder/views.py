from django.shortcuts import render
import pandas as pd
import numpy as np
from django.http import JsonResponse
from atmPostService.models import Transaccion, Cajero, eCode
import datetime as dt



# Create your views here.
def index(request):
    return render(request, 'index.html')

def options(request):
    return render(request, 'options.html')

def ecode(request):
    return render(request, 'eCode.html')

def cuestionario(request):
    return render(request, 'cuestionario.html')

def charts(request):
    return render(request, 'charts.html')

def POST_ecode2tran(request):
    ecode = request.POST.get('ecode')
    ecode = eCode.objects.filter(ecode = ecode).first()
    return JsonResponse({'success':True,'id_transaccion':ecode.id_trans})

def POST_cuestionario(request):
    print('entro')
    tipo = request.POST.get('tipo', None)
    fecha = request.POST.get('fecha', None)
    hora = request.POST.get('hora', None)
    estado = request.POST.get('estado', None)
    municipio = request.POST.get('municipio', None)
    ultimos_digitos = request.POST.get('u4', None)
    banco = request.POST.get('banco', None)

    df = pd.DataFrame(list(Transaccion.objects.filter(tipo = tipo).values()))
    print(df.head())
    if fecha is not "empty":
        fecha = dt.datetime(int(fecha[:4]), int(fecha[5:7]), int(fecha[8:]))
        lista=[]
        bool_list = []
        for i in df["fecha"]:   
            i.to_pydatetime()
            i=dt.datetime(i.year,i.month,i.day)
            lista.append(i)
        df_fecha=pd.DataFrame(lista,columns=["fecha"])
        for i in df_fecha['fecha']:
            print(i)
            print(fecha)
            x = (i.year == fecha.year) and (i.month == fecha.month) and (i.day == fecha.day)
            bool_list.append(x)
    if hora is not "empty":
        rango  = define_hora(hora)
        serie=df["fecha"]
        for i in serie:
            i=dt.datetime.time(i)
        #filtro_hora=list(rango[0]-dt.timedelta(minutes=15)<serie<rango[1]+dt.timedelta(minutes=15))
        #filtro_hora=list(rango[0]<serie and serie<rango[1])
        filtro_hora = []
        for i in serie:
            print(i)
            print(rango[0])
            x = rango[0].hour<i.hour and i.hour<rango[1].hour
            filtro_hora.append(x)

    # if estado is not "empty":
    #     print(pd.DataFrame(list(Cajero.objects.filter(estado = estado).values())))
    #     cajeros = pd.DataFrame(list(Cajero.objects.filter(estado = estado).values()))['id_atm']
    #     filtro_cajero = df[df['id_atm'] in cajeros]
    # if municipio is not "empty":
    #     cajeros = pd.DataFrame(list(Cajero.objects.filter(municipio = municipio).values()))['id_atm']
    #     filtro_cajero = df[df['id_atm'] in cajeros]
        
    # if ultimos_digitos is not "empty":
    #     filtro_cuenta = df[df['cuenta'][-4:] == ultimos_digitos]
    # if banco is not "empty":
    #     filtro_banco = df[df['banco'] == banco]
    
    #print(df[np.logical_and(filtro_fecha,np.logical_and(filtro_banco,filtro_cuenta))])
    
    response = {'success': True, 'id_transaccion': "D100112345201899"}

    return JsonResponse(response)



def define_hora(hora):
    h1=hora[0:2]
    h2=hora[3:5]
    dt_hora1=dt.time(hour=int(h1))
    dt_hora2=dt.time(hour=int(h2))
    rango=[dt_hora1,dt_hora2]
    return rango
    