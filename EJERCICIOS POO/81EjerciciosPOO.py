# Solución ejercicio 82: Mini sistema de tareas con persistencia JSON
import json, os
class Tareas:
    def __init__(self,path='/mnt/data/tareas.json'): self.path = path; self.tareas = []
    def add(self,t): self.tareas.append(t); self._save()
    def _save(self): with open(self.path,'w') as f: json.dump(self.tareas,f)

if __name__ == '__main__':
    t = Tareas(); t.add({'titulo':'Pagar'}); print('Guardado', t.path)
