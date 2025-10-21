# Solución ejercicio 25: Clase con __str__ y __repr__ para representación
class Persona:
    def __init__(self,n): self.n=n
    def __str__(self): return f"Persona: {self.n}"
    def __repr__(self): return f"Persona({self.n!r})"

if __name__ == '__main__':
    p = Persona('Ana'); print(p); print(repr(p))
