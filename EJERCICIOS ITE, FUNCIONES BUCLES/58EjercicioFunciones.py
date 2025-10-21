# Solución ejercicio 61: año bisiesto
def es_bisiesto(a):
    return (a%4==0 and a%100!=0) or (a%400==0)

if __name__ == '__main__':
    print(es_bisiesto(2020))
    print(es_bisiesto(1900))
