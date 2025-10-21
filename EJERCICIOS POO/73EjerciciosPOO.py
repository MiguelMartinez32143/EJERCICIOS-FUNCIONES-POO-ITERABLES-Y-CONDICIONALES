# Solución ejercicio 75: Clase que usa callback al completar tarea
class Tarea:
    def __init__(self,cb=None): self.cb=cb
    def completar(self):
        if self.cb: self.cb('hecho'); return 'OK'

if __name__ == '__main__':
    t = Tarea(lambda m: print('callback',m)); t.completar()
