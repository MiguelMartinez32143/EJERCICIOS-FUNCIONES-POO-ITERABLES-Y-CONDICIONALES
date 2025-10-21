# Solución ejercicio 10: Mascota con estados de ánimo y acciones
class Mascota:
    def __init__(self,nombre, especie):
        self.nombre = nombre; self.especie = especie; self.animo = 'Feliz'
    def alimentar(self):
        self.animo = 'Satisfecho'; return self.animo
    def jugar(self):
        self.animo = 'Animado'; return self.animo
    def dormir(self):
        self.animo = 'Durmiendo'; return self.animo

if __name__ == '__main__':
    m = Mascota('Max','Perro')
    print(m.alimentar(), m.jugar(), m.dormir())
