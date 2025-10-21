# Solución ejercicio 86: Clase que implementa retry simple para operaciones que pueden fallar
import time
class Retry:
    def __init__(self,tries=3): self.tries=tries
    def run(self,fn,*a,**k):
        for i in range(self.tries):
            try: return fn(*a,**k)
            except Exception as e:
                if i==self.tries-1: raise
                time.sleep(0.01)

if __name__ == '__main__':
    r = Retry(); print(r.run(lambda: 1/1))
