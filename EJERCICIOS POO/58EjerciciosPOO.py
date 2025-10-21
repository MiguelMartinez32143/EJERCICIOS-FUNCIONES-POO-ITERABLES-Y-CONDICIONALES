# Solución ejercicio 61: Clase que implementa búsqueda por atributo en lista de objetos
class Usuario:
    def __init__(self,n,id): self.nombre=n; self.id=id

def buscar_por_nombre(lista, nombre):
    for u in lista:
        if u.nombre == nombre: return u
    return None

if __name__ == '__main__':
    us = [Usuario('Ana',1), Usuario('Luis',2)]; print(buscar_por_nombre(us,'Luis').id)
