# Solución ejercicio 43: reduce para producto
from functools import reduce
def reduce_producto(lista):
    return reduce(lambda a,b: a*b, lista, 1)

if __name__ == '__main__':
    print(reduce_producto([2,3,4]))
