# Solución ejercicio 25: dividir con chequeo de división por cero
def dividir(a,b):
    if b == 0:
        return None
    return a / b

if __name__ == '__main__':
    print(dividir(10,2))
    print(dividir(1,0))
