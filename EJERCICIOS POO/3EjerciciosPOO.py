# Solución ejercicio 11: Animal y subclases Perro/Gato (herencia básica)
class Animal:
    def __init__(self,nombre): self.nombre = nombre
    def hacer_sonido(self): return '...'

class Perro(Animal):
    def __init__(self,nombre, raza): super().__init__(nombre); self.raza = raza
    def hacer_sonido(self): return 'Guau'

class Gato(Animal):
    def hacer_sonido(self): return 'Miau'

if __name__ == '__main__':
    p = Perro('Fido','Labrador'); g = Gato('Garfield')
    print(p.hacer_sonido(), g.hacer_sonido())
