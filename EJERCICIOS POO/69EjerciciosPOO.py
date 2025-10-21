# Solución ejercicio 71: Patrón Repository simple con búsqueda y listado
class Repo:
    def __init__(self): self._data = {}
    def add(self,k,v): self._data[k]=v
    def all(self): return list(self._data.values())

if __name__ == '__main__':
    r=Repo(); r.add('a',1); print(r.all())
