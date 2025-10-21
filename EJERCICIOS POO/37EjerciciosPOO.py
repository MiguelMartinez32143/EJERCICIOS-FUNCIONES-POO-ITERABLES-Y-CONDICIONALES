# Solución ejercicio 42: Introspección: listar atributos y métodos de un objeto
class Demo: 
    def __init__(self): self.a = 1
    def m(self): pass

if __name__ == '__main__':
    d = Demo(); print([x for x in dir(d) if not x.startswith('__')])
