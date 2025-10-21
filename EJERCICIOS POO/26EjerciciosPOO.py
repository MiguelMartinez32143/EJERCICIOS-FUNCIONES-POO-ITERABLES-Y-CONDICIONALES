# Solución ejercicio 32: Mixins para añadir funcionalidad reutilizable
class ToDictMixin:
    def to_dict(self): return self.__dict__

class Persona(ToDictMixin):
    def __init__(self,n): self.n=n

if __name__ == '__main__':
    print(Persona('Ana').to_dict())
