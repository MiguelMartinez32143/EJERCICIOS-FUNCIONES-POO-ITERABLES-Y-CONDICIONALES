# Solución ejercicio 36: generador contador hasta n
def contador_hasta(n):
    i = 1
    while i <= n:
        yield i
        i += 1

if __name__ == '__main__':
    for x in contador_hasta(3):
        print(x)
