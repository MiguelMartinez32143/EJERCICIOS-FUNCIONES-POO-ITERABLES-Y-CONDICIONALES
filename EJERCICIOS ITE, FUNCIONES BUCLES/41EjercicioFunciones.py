# Solución ejercicio 46: recursión con caso base
def contar(n):
    if n <= 0:
        return 0
    return n + contar(n-1)

if __name__ == '__main__':
    print(contar(3))
