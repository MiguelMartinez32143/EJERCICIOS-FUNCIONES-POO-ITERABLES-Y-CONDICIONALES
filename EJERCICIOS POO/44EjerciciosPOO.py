# Solución ejercicio 49: Método factory alternativo con @classmethod
class Persona:
    def __init__(self,nombre): self.nombre=nombre
    @classmethod
    def desde_nombre_completo(cls, full):
        nombre = full.split()[0]; return cls(nombre)

if __name__ == '__main__':
    p = Persona.desde_nombre_completo('Ana Pérez'); print(p.nombre)
