# Solución ejercicio 12: filtrar pares de una lista
def filtrar_pares(lista):
    return [x for x in lista if x % 2 == 0]

if __name__ == '__main__':
    print(filtrar_pares([1,2,3,4,5,6]))
