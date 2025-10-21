# Solución ejercicio 12: Vehículo y subclases Auto/Moto mostrando sobreescritura
class Vehiculo:
    def __init__(self,marca,modelo): self.marca = marca; self.modelo = modelo; self.vel = 0
    def acelerar(self,inc): self.vel += inc; return self.vel

class Auto(Vehiculo):
    def acelerar(self,inc): self.vel += inc*1.2; return self.vel

class Moto(Vehiculo):
    def acelerar(self,inc): self.vel += inc*1.5; return self.vel

if __name__ == '__main__':
    a = Auto('Toyota','C'); m = Moto('Yamaha','M')
    print(a.acelerar(10), m.acelerar(10))
