# Solución ejercicio 23: Polimorfismo con figuras geométricas
class Figura:
    def area(self): raise NotImplementedError
class Circulo(Figura):
    def __init__(self,r): self.r=r
    def area(self): return 3.1416*self.r*self.r
class Cuadrado(Figura):
    def __init__(self,l): self.l=l
    def area(self): return self.l*self.l

if __name__ == '__main__':
    fig = [Circulo(2), Cuadrado(3)]
    for f in fig: print(f.area())
