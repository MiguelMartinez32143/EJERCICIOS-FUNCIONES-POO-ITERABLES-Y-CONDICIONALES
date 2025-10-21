# Solución ejercicio 2: función que verifica si un número es impar
def es_impar(n):
    return n % 2 != 0

if __name__ == '__main__':
    print(es_impar(3))
    print(es_impar(8))
