# Solución ejercicio 80: Clase que mantiene referencias débiles a callbacks (uso de weakref.WeakSet)
import weakref
class Manager:
    def __init__(self): self._refs = weakref.WeakSet()
    def add(self,o): self._refs.add(o)
    def count(self): return len(self._refs)

if __name__ == '__main__':
    class A: pass
    m=Manager(); a=A(); m.add(a); print(m.count())
