# Solución ejercicio 99: memoización manual
def memoize_manual(func):
    cache={}
    def wrapper(n):
        if n in cache: return cache[n]
        cache[n]=func(n)
        return cache[n]
    return wrapper

@memoize_manual
def fib(n):
    if n<2: return n
    return fib(n-1)+fib(n-2)

if __name__ == '__main__':
    print(fib(20))
