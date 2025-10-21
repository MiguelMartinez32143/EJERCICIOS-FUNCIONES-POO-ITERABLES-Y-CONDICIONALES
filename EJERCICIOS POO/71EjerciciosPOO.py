# Solución ejercicio 73: Clase que implementa 'copy' method para clonar
class Person:
    def __init__(self,n): self.n=n
    def copy(self): return Person(self.n)

if __name__ == '__main__':
    p=Person('Ana'); q=p.copy(); print(q.n)
