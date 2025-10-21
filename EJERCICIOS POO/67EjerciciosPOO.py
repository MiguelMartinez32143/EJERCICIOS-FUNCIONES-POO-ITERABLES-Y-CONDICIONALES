# Solución ejercicio 6: Estudiante que gestiona calificaciones y promedio
class Estudiante:
    def __init__(self, nombre, id_estudiante):
        self.nombre = nombre
        self.id_estudiante = id_estudiante
        self.calificaciones = []

    def agregar_calificacion(self, cal):
        if 0<=cal<=100:
            self.calificaciones.append(cal)
            return True
        return False

    def obtener_promedio(self):
        if not self.calificaciones: return None
        return sum(self.calificaciones)/len(self.calificaciones)

if __name__ == '__main__':
    e = Estudiante('Ana', 'E101')
    e.agregar_calificacion(85); e.agregar_calificacion(90)
    print(e.obtener_promedio())
