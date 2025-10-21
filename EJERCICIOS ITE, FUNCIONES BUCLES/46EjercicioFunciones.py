# Solución ejercicio 50: generador fibonacci que produce n primeros
def generador_fibonacci(n):
    a,b = 0,1
    for _ in range(n):
        yield a
        a,b = b,a+b

if __name__ == '__main__':
    print(list(generador_fibonacci(8)))
