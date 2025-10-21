# Solución ejercicio 5: sumar varios argumentos
def sumar(*numeros):
    return sum(numeros)

if __name__ == '__main__':
    print(sumar(1, 2, 3))
