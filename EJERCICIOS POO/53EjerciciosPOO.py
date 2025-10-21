# Solución ejercicio 57: Implementar patrón Adapter (adaptar interfaz)
class Viejo:
    def viejo(self): return 'viejo'
class Adapter:
    def __init__(self,v): self.v=v
    def nuevo(self): return self.v.viejo()

if __name__ == '__main__':
    print(Adapter(Viejo()).nuevo())
