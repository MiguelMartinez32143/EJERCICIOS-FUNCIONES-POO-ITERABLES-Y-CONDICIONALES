# Solución ejercicio 39: uso de parámetros posicionales-only y keyword-only
def funcion(a, b, /, c, *, d):
    return a + b + c + d

if __name__ == '__main__':
    print(funcion(1,2,3,d=4))
