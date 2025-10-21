# Solución ejercicio 56: Clases con dependencias inyectadas (DI simple)
class Servicio:
    def operar(self): return 'ok'
class Consumidor:
    def __init__(self, servicio): self.servicio = servicio
    def run(self): return self.servicio.operar()

if __name__ == '__main__':
    print(Consumidor(Servicio()).run())
