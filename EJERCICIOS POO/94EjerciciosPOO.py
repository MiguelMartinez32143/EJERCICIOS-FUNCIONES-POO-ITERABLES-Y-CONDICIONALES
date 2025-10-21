# Solución ejercicio 94: Clase que implementa prioridad simple (heap) para tareas
import heapq
class TaskQueue:
    def __init__(self): self._heap=[]
    def push(self,priority,task): heapq.heappush(self._heap,(priority,task))
    def pop(self): return heapq.heappop(self._heap)[1]

if __name__ == '__main__':
    q = TaskQueue(); q.push(1,'A'); q.push(0,'B'); print(q.pop())
