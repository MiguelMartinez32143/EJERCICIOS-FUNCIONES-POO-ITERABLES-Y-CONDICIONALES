# Solución ejercicio 34: Factory method para crear objetos según tipo
class Animal: pass
class Perro(Animal): pass
class Gato(Animal): pass

def crear(tipo, nombre):
    if tipo=='perro': return Perro()
    if tipo=='gato': return Gato()
    return None

if __name__ == '__main__':
    print(type(crear('perro')))
