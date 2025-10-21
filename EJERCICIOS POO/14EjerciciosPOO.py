# Solución ejercicio 21: Clase abstracta Vehiculo y subclases que implementan métodos abstractos
from abc import ABC, abstractmethod

class Vehiculo(ABC):
    @abstractmethod
    def acelerar(self): pass

class Auto(Vehiculo):
    def __init__(self): self.vel = 0
    def acelerar(self): self.vel += 10; return self.vel

if __name__ == '__main__':
    a = Auto(); print(a.acelerar())
