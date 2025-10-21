# Solución ejercicio 70: Clase con método para convertir a dict (serialización simple)
class Persona:
    def __init__(self,n,a): self.nombre=n; self.edad=a
    def to_dict(self): return {'nombre':self.nombre,'edad':self.edad}

if __name__ == '__main__':
    print(Persona('Ana',30).to_dict())
