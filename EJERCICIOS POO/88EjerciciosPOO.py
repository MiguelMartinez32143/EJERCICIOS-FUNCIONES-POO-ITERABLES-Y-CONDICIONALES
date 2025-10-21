# Solución ejercicio 89: Clase que usa enum para estados
from enum import Enum
class Estado(Enum):
    INICIO = 1; PROCESO = 2; FIN = 3

if __name__ == '__main__':
    print(Estado.INICIO, Estado.FIN.name)
