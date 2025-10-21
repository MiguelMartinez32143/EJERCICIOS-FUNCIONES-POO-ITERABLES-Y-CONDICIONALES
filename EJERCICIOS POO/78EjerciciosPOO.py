# Solución ejercicio 7: Libro con estado de préstamo
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponible = True

    def prestar(self):
        if not self.disponible: return 'No disponible'
        self.disponible = False
        return f"'{self.titulo}' prestado"

    def devolver(self):
        if self.disponible: return 'Ya está en biblioteca'
        self.disponible = True
        return f"'{self.titulo}' devuelto"

if __name__ == '__main__':
    l = Libro('Cien años', 'G.G.M.')
    print(l.prestar()); print(l.devolver())
