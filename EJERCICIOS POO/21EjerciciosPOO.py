# Solución ejercicio 28: Uso de __slots__ para ahorrar memoria
class ConSlots:
    __slots__ = ('a','b')
    def __init__(self,a,b): self.a=a; self.b=b

if __name__ == '__main__':
    s = ConSlots(1,2); print(s.a,s.b)
