# Solución ejercicio 69: Clase con memoización interna para método costoso
class Fib:
    def __init__(self): self.cache = {0:0,1:1}
    def calc(self,n):
        if n in self.cache: return self.cache[n]
        self.cache[n] = self.calc(n-1)+self.calc(n-2)
        return self.cache[n]

if __name__ == '__main__':
    print(Fib().calc(20))
