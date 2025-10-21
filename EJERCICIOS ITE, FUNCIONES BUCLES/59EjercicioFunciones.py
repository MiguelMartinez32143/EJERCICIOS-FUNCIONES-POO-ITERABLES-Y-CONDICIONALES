# Solución ejercicio 62: diferencia en días entre dos fechas YYYY-MM-DD
from datetime import datetime
def dias_entre(f1,f2):
    fmt="%Y-%m-%d"
    d1=datetime.strptime(f1,fmt); d2=datetime.strptime(f2,fmt)
    return abs((d2-d1).days)

if __name__ == '__main__':
    print(dias_entre("2020-01-01","2020-01-10"))
