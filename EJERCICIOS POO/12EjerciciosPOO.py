# Solución ejercicio 1: Clase Persona básica con métodos saludar y cumplir años
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        return f"Hola, mi nombre es {self.nombre}."

    def cumplir_anios(self):
        self.edad += 1
        return f"¡Feliz cumpleaños, {self.nombre}! Ahora tienes {self.edad} años."

if __name__ == '__main__':
    p = Persona('Ana', 30)
    print(p.saludar())
    print(p.cumplir_anios())
