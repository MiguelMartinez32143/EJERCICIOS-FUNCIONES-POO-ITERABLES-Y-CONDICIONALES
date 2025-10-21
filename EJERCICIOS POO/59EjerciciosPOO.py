# Solución ejercicio 62: Clase que implementa ordenamiento por atributo
class Item:
    def __init__(self,name,valor): self.name=name; self.valor=valor

if __name__ == '__main__':
    items = [Item('a',5), Item('b',2)]
    items.sort(key=lambda x: x.valor)
    print([i.name for i in items])
