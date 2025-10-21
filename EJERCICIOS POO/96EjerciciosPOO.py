# Solución ejercicio 96: Clase que calcula estadísticas simples de una serie de números
class Stats:
    def __init__(self): self.nums = []
    def add(self,x): self.nums.append(x)
    def mean(self): return sum(self.nums)/len(self.nums) if self.nums else 0

if __name__ == '__main__':
    s = Stats(); s.add(1); s.add(3); print(s.mean())
