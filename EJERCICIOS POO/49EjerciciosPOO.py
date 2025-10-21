# Solución ejercicio 53: Clase configurable con argumentos **kwargs
class Config:
    def __init__(self, **kwargs):
        for k,v in kwargs.items(): setattr(self,k,v)

if __name__ == '__main__':
    c = Config(a=1,b=2); print(c.a, c.b)
