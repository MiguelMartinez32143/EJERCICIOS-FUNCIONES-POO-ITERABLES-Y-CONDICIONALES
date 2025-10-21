# Solución ejercicio 16: Método de clase y método estático
class Circulo:
    PI = 3.1416
    def __init__(self,radio): self.radio=radio
    @classmethod
    def desde_diametro(cls,d): return cls(d/2)
    @staticmethod
    def area_formula(r): return Circulo.PI * r*r

if __name__ == '__main__':
    c = Circulo.desde_diametro(10)
    print(c.radius if hasattr(c,'radius') else c.radio)
    print(Circulo.area_formula(5))
