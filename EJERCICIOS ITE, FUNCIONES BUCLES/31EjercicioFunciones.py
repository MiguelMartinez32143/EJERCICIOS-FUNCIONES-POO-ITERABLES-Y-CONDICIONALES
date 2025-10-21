# Solución ejercicio 37: generador numeros pares hasta un maximo
def numeros_pares_generador(maximo):
    n = 0
    while n <= maximo:
        if n % 2 == 0:
            yield n
        n += 1

if __name__ == '__main__':
    print(list(numeros_pares_generador(10)))
