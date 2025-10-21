# Solución ejercicio 9: Rectángulo con cálculo de área y perímetro
class Rectangulo:
    def __init__(self,largo,ancho):
        if largo<=0 or ancho<=0: raise ValueError('Dimensiones inválidas')
        self.largo = largo; self.ancho = ancho
    def area(self): return self.largo*self.ancho
    def perimetro(self): return 2*(self.largo+self.ancho)

if __name__ == '__main__':
    r = Rectangulo(10,5)
    print(r.area(), r.perimetro())
