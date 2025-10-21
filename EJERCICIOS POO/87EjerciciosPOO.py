# Solución ejercicio 88: Clase que implementa throttling sencillo (limitar llamadas)
import time
class Throttle:
    def __init__(self, per_second): self.per_second=per_second; self.last=0
    def allow(self):
        now=time.time()
        if now - self.last >= 1/self.per_second:
            self.last = now; return True
        return False

if __name__ == '__main__':
    t = Throttle(2); print(t.allow()); print(t.allow())
