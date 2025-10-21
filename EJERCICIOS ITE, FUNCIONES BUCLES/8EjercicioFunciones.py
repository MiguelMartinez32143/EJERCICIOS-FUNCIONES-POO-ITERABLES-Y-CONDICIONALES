# Solución ejercicio 16: generador de primos indefinido
def es_primo(n):
    if n < 2: return False
    i=2
    while i*i <= n:
        if n % i == 0:
            return False
        i+=1
    return True

def generador_primos():
    n = 2
    while True:
        if es_primo(n):
            yield n
        n += 1

if __name__ == '__main__':
    g = generador_primos()
    print(next(g), next(g), next(g), next(g))
