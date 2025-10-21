# Solución ejercicio 13: Empleado con subclases Gerente y Desarrollador (polimorfismo)
class Empleado:
    def __init__(self,nombre,salario): self.nombre=nombre; self.salario=salario
    def calcular_bonus(self): return 0

class Gerente(Empleado):
    def calcular_bonus(self): return self.salario*0.15

class Desarrollador(Empleado):
    def calcular_bonus(self): return self.salario*0.10

if __name__ == '__main__':
    g = Gerente('Iván',3000); d = Desarrollador('Ana',2500)
    print(g.calcular_bonus(), d.calcular_bonus())
