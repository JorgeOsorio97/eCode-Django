from atmPostService.models import eCode, Transacciones, Cajero, Cuenta

def define(x):
    if x < 10 :
        i = str(x)
    else:
        if x == 10:
            i = 'A'
        elif x == 11:
            i = 'B'
        elif x == 12:
            i = 'C'
        elif x == 13:
            i = 'D'
        elif x == 14:
            i = 'E'
        elif x == 15:
            i = 'F'
        elif x == 16:
            i = 'G'
        elif x == 17:
            i = 'H'
        elif x == 18:
            i = 'I'
        elif x == 19:
            i = 'J'
        elif x == 20:
            i = 'K'
        elif x == 21:
            i = 'L'
        elif x == 22:
            i = 'M'
        elif x == 23:
            i = 'N'
        elif x == 24:
            i = 'O'
        elif x == 25:
            i = 'P'
        elif x == 26:
            i = 'Q'
        elif x == 27:
            i = 'R'
        elif x == 28:
            i = 'S'
        elif x == 29:
            i = 'T'
        elif x == 30:
            i = 'U'
        elif x == 31:
            i = 'V'
        elif x == 32:
            i = 'W'
        elif x == 33:
            i = 'X'
        elif x == 34:
            i = 'Y'
        elif x == 35:
            i = 'Z'
        
    return i
def poblar():
    n=0
    ecode = [0,0,0,0,0]
    for x in range(36):
        ecode[0] = (define(x))
        for y in range(36):
            ecode[1] = (define(y))
            for z in range(36):
                ecode[2] = (define(z))
                for a in range(36):
                    ecode[3] = (define(a))
                    for b in range(36):
                        ecode[4] = (define(b))
                        sqlappend = eCode(ecode = ecode[0]+ecode[1]+ecode[2]+ecode[3]+ecode[4], id_transaccion = None)
                        sqlappend.save()
                        n+=1
                        print(n)
                    
def poblar_cuentas():
    for x in range(100):
        return

def poblar_transacciones():
    for x in range(10000):
        return