# Solución ejercicio 22: decorador que repite ejecución N veces
from functools import wraps

def repetir(veces=1):
    def decorador(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            resultado = None
            for _ in range(veces):
                resultado = func(*args, **kwargs)
            return resultado
        return wrapper
    return decorador

@repetir(3)
def hola():
    print("hola")

if __name__ == '__main__':
    hola()
