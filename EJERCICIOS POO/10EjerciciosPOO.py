# Solución ejercicio 18: Decorador simple para medir tiempo (aplicable a métodos)
import time, functools
def medir_tiempo(func):
    @functools.wraps(func)
    def wrapper(*a,**k):
        t0 = time.time(); r = func(*a,**k); t1 = time.time()
        print(f"{func.__name__} tardó {t1-t0:.6f}s"); return r
    return wrapper

class Demo:
    @medir_tiempo
    def trabajo(self,n): sum(range(n))

if __name__ == '__main__':
    d=Demo(); d.trabajo(100000)
