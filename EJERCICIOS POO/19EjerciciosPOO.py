# Solución ejercicio 26: Operator overloading (__add__ para sumar objetos)
class Punto:
    def __init__(self,x,y): self.x=x; self.y=y
    def __add__(self,other): return Punto(self.x+other.x, self.y+other.y)
    def __repr__(self): return f'Punto({self.x},{self.y})'

if __name__ == '__main__':
    a = Punto(1,2); b = Punto(3,4); print(a+b)
