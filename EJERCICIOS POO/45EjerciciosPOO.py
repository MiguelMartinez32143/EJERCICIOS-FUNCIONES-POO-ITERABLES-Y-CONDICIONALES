# Solución ejercicio 4: Vehículo con acelerar/frenar y validación
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0

    def acelerar(self, inc):
        if inc>0:
            self.velocidad += inc
            return f"Velocidad: {self.velocidad} km/h"
        return 'Incremento debe ser positivo'

    def frenar(self, dec):
        if dec>0:
            self.velocidad = max(0, self.velocidad-dec)
            return f"Velocidad: {self.velocidad} km/h"
        return 'Decremento debe ser positivo'

if __name__ == '__main__':
    v = Vehiculo('Toyota','Corolla')
    print(v.acelerar(50))
    print(v.frenar(20))
