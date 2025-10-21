# Solución ejercicio 46: Implementación básica de iterator en una clase
class Contenedor:
    def __init__(self,data): self.data = data
    def __iter__(self): return iter(self.data)

if __name__ == '__main__':
    for x in Contenedor([1,2,3]): print(x)
