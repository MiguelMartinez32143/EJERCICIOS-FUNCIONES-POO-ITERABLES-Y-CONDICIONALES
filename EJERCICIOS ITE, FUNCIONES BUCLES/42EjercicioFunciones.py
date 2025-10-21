# Solución ejercicio 47: memoización con lru_cache (ejemplo)
from functools import lru_cache

@lru_cache(maxsize=None)
def ejemplo(n):
    if n < 2: return n
    return ejemplo(n-1) + ejemplo(n-2)

if __name__ == '__main__':
    print(ejemplo(20))
