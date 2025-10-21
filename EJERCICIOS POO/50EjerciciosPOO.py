# Solución ejercicio 54: Implementar método __len__ y __contains__ para clase contenedor
class MiCont:
    def __init__(self, data): self._data = list(data)
    def __len__(self): return len(self._data)
    def __contains__(self, item): return item in self._data

if __name__ == '__main__':
    c = MiCont([1,2,3]); print(len(c), 2 in c)
