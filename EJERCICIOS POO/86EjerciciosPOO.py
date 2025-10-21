# Solución ejercicio 87: Clase que implementa caching simple con decorador de método
from functools import wraps
def method_cache(fn):
    cache = {}
    @wraps(fn)
    def wrapper(self, *a):
        key = (a)
        if key in cache: return cache[key]
        cache[key] = fn(self, *a); return cache[key]
    return wrapper

class Calc:
    @method_cache
    def fib(self,n):
        if n<2: return n
        return self.fib(n-1)+self.fib(n-2)

if __name__ == '__main__':
    print(Calc().fib(20))
