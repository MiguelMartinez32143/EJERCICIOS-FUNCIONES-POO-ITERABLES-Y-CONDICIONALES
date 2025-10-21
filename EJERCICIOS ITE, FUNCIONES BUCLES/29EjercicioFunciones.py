# Solución ejercicio 35: medir tiempo con decorador
import time
from functools import wraps

def medir_tiempo(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        fin = time.time()
        print(f"{func.__name__} tardó {fin-inicio:.6f}s")
        return resultado
    return wrapper

@medir_tiempo
def suma_n(n):
    return sum(range(n))

if __name__ == '__main__':
    suma_n(100000)
