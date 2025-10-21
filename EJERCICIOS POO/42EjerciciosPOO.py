# Solución ejercicio 47: Ejemplo de property calculada (solo getter)
class Persona:
    def __init__(self, nombre, año_nac): self.nombre=nombre; self.año=año_nac
    @property
    def edad(self): import datetime; return datetime.datetime.now().year - self.año

if __name__ == '__main__':
    p = Persona('Ana', 2000); print(p.edad)
