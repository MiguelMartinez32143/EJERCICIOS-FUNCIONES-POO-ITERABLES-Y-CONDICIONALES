# Solución ejercicio 58: Clase que expone método fluent (encadenamiento)
class Builder:
    def __init__(self): self.items=[]
    def add(self,x): self.items.append(x); return self
    def result(self): return self.items

if __name__ == '__main__':
    b = Builder().add(1).add(2); print(b.result())
