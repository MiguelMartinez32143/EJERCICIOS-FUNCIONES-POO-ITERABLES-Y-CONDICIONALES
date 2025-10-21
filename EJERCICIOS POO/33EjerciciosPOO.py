# Solución ejercicio 39: Composición con listas de objetos y método para mostrar
class Tarea:
    def __init__(self,desc): self.desc=desc
class Proyecto:
    def __init__(self): self.tareas=[]
    def agregar(self,t): self.tareas.append(t)
    def mostrar(self): return [t.desc for t in self.tareas]

if __name__ == '__main__':
    p = Proyecto(); p.agregar(Tarea('A')); print(p.mostrar())
