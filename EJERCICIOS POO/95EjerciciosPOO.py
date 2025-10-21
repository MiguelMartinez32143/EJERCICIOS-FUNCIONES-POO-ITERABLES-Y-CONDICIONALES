# Solución ejercicio 95: Clase que valida y normaliza entrada en constructor
class Persona:
    def __init__(self,nombre, edad):
        nombre = nombre.strip().title()
        if edad < 0: raise ValueError('Edad negativa')
        self.nombre = nombre; self.edad = edad

if __name__ == '__main__':
    p = Persona(' ana ', 20); print(p.nombre, p.edad)
