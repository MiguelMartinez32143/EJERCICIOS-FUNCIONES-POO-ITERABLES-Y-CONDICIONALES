# Solución ejercicio 79: Implementar método to_string y from_string (serialización textual)
class Punto:
    def __init__(self,x,y): self.x=x; self.y=y
    def to_string(self): return f"{self.x},{self.y}"
    @classmethod
    def from_string(cls,s): x,y = map(int,s.split(',')); return cls(x,y)

if __name__ == '__main__':
    p=Punto.from_string('3,4'); print(p.to_string())
