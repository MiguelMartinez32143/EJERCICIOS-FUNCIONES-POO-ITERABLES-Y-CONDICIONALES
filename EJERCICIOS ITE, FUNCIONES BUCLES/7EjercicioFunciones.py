# Solución ejercicio 15: fibonacci con cache (lru_cache)
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_cache(n):
    if n < 2:
        return n
    return fibonacci_cache(n-1) + fibonacci_cache(n-2)

if __name__ == '__main__':
    print(fibonacci_cache(30))
