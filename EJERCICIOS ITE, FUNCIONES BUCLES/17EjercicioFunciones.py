# Solución ejercicio 24: factorial con memo (lru_cache)
from functools import lru_cache

@lru_cache(maxsize=None)
def factorial_memo(n):
    if n <= 1:
        return 1
    return n * factorial_memo(n-1)

if __name__ == '__main__':
    print(factorial_memo(10))
