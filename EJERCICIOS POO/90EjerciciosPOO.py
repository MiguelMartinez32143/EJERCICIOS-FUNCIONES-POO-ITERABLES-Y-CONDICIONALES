# Solución ejercicio 90: Clase que implementa registro de cambios (observer simple)
class Observable:
    def __init__(self): self._obs=[]
    def subscribe(self,o): self._obs.append(o)
    def change(self,val): [o(val) for o in self._obs]

if __name__ == '__main__':
    o = Observable(); o.subscribe(lambda v: print('Cambio',v)); o.change(5)
