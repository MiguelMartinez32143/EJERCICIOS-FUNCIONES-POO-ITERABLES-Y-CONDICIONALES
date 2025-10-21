# Solución ejercicio 68: Clase con método que devuelve iterator propio (yield)
class Contador:
    def __init__(self,n): self.n=n
    def __iter__(self):
        i = 0
        while i < self.n:
            yield i; i+=1

if __name__ == '__main__':
    for x in Contador(3): print(x)
