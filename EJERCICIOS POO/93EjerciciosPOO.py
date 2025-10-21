# Solución ejercicio 93: Clase que registra tiempo de creación de instancias (timestamp)
import datetime
class Item:
    def __init__(self): self.created = datetime.datetime.now()

if __name__ == '__main__':
    i = Item(); print(i.created.isoformat())
