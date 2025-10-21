# Solución ejercicio 42: filter con lambda pares
def filter_pares(lista):
    return list(filter(lambda x: x%2==0, lista))

if __name__ == '__main__':
    print(filter_pares([1,2,3,4]))
