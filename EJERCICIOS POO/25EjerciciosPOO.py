# Solución ejercicio 31: Descriptor simple (validador de entero positivo)
class Positivo:
    def __init__(self): self.data = {}
    def __get__(self, obj, objtype): return self.data.get(obj)
    def __set__(self, obj, val):
        if not isinstance(val,int) or val<0: raise ValueError('Debe ser int >=0')
        self.data[obj] = val

class Producto:
    precio = Positivo()
    def __init__(self, p): self.precio = p

if __name__ == '__main__':
    prod = Producto(10); print(prod.precio)
