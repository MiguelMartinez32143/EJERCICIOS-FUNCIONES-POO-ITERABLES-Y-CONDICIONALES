# Solución ejercicio 100: Pequeña API interna de Alumnos con agregar/mostrar/mejor
class SistemaAlumnos:
    def __init__(self): self.alumnos = {}
    def agregar(self,nombre,nota): self.alumnos[nombre]=nota
    def mostrar(self): return dict(self.alumnos)
    def mejor(self): return max(self.alumnos.items(), key=lambda kv: kv[1]) if self.alumnos else None

if __name__ == '__main__':
    s = SistemaAlumnos(); s.agregar('Ana',9); s.agregar('Luis',7)
    print(s.mostrar()); print(s.mejor())
