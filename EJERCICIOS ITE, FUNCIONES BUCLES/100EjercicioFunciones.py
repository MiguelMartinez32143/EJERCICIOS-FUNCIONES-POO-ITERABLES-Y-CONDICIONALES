# Solución ejercicio 9: promedio de argumentos
def promedio(*args):
    if not args:
        return 0
    return sum(args) / len(args)

if __name__ == '__main__':
    print(promedio(2,4,6))
