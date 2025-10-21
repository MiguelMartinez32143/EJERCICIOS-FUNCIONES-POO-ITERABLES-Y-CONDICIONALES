# Solución ejercicio 20: Agregación (lista de objetos dentro de otro)
class Estudiante:
    def __init__(self,nombre): self.nombre = nombre
class Curso:
    def __init__(self,nombre): self.nombre=nombre; self.alumnos=[]
    def inscribir(self,est): self.alumnos.append(est)

if __name__ == '__main__':
    c = Curso('POO'); e = Estudiante('Ana'); c.inscribir(e); print([al.nombre for al in c.alumnos])
