# Solución ejercicio 49: decorador que preserva metadatos (usa wraps)
from functools import wraps
def ejemplo_decorador(func):
    @wraps(func)
    def wrapper(*a, **k):
        return func(*a, **k)
    return wrapper

if __name__ == '__main__':
    @ejemplo_decorador
    def f(): return 'ok'
    print(f())
