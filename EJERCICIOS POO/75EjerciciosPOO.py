# Solución ejercicio 77: Ejemplo de método que devuelve función (closure desde objeto)
class C:
    def __init__(self,x): self.x=x
    def make_adder(self):
        def add(y): return self.x + y
        return add

if __name__ == '__main__':
    f = C(5).make_adder(); print(f(3))
