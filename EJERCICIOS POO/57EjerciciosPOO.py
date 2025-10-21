# Solución ejercicio 60: Clase para manejo de recursos con método close (no context manager)
class RecursoSimple:
    def __init__(self): self.abierto = True
    def close(self): self.abierto = False

if __name__ == '__main__':
    r = RecursoSimple(); r.close(); print(r.abierto)
