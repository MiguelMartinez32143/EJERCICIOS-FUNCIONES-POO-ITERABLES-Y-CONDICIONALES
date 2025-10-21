# Solución ejercicio 19: Composición (una clase contiene objetos de otra)
class Motor:
    def __init__(self, potencia): self.potencia = potencia
class Auto:
    def __init__(self, marca, motor: Motor): self.marca = marca; self.motor = motor

if __name__ == '__main__':
    m = Motor(120); a = Auto('Ford', m); print(a.motor.potencia)
