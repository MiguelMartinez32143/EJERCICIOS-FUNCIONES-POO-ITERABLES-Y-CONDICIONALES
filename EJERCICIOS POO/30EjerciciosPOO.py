# Solución ejercicio 36: Registro de instancias (atributo de clase que cuenta instancias)
class Contador:
    total = 0
    def __init__(self): Contador.total += 1

if __name__ == '__main__':
    Contador(); Contador(); print(Contador.total)
