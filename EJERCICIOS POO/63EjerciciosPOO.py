# Solución ejercicio 66: Clase que mantiene contador por instancia y total global
class Item:
    total = 0
    def __init__(self): Item.total += 1; self.id = Item.total

if __name__ == '__main__':
    a=Item(); b=Item(); print(a.id, b.id, Item.total)
