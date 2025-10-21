# Solución ejercicio 41: Clonación (shallow copy) y deepcopy ejemplo
import copy
class Demo: 
    def __init__(self, lista): self.lista = lista

if __name__ == '__main__':
    d = Demo([1,2]); s = copy.copy(d); deep = copy.deepcopy(d)
    d.lista.append(3); print(s.lista, deep.lista)
