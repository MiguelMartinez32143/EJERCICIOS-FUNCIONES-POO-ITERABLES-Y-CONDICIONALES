# Solución ejercicio 98: Clase que implementa limitador de tamaño para lista interna
class BoundedList:
    def __init__(self,limit): self.limit=limit; self.data=[]
    def append(self,x):
        if len(self.data) >= self.limit: self.data.pop(0)
        self.data.append(x)

if __name__ == '__main__':
    b = BoundedList(2); b.append(1); b.append(2); b.append(3); print(b.data)
