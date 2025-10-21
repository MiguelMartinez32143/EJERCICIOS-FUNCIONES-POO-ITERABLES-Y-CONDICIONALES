# Solución ejercicio 14: Clase con atributos de clase y de instancia
class Estudiante:
    escuela = 'SENA'
    def __init__(self,nombre): self.nombre = nombre

if __name__ == '__main__':
    e1 = Estudiante('Ana'); e2 = Estudiante('Luis')
    print(Estudiante.escuela, e1.nombre, e2.nombre)
