# Solución ejercicio 13: decorador debug que muestra args y resultado
from functools import wraps

def decorador_debug(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"LLAMADA {func.__name__} args={args} kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"RESULTADO {func.__name__} -> {resultado}")
        return resultado
    return wrapper

@decorador_debug
def suma(a,b):
    return a+b

if __name__ == '__main__':
    suma(2,3)
