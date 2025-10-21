# Solución ejercicio 6: multiplicar varios argumentos
def multiplicar_varios(*args):
    prod = 1
    for n in args:
        prod *= n
    return prod

if __name__ == '__main__':
    print(multiplicar_varios(2,3,4))
