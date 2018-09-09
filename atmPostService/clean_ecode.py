from atmPostService.models import eCode 
import datetime.datetime

def clean():
    ecodes_usados = eCode.objects.filter(id_transaccion__isnull = True)

    for ecode in ecodes_usados:
        if datetime.datetime.now()-ecode.fecha_uso>7:
            ecode.id_transaccion = None
            ecode.fecha_uso = None
        

