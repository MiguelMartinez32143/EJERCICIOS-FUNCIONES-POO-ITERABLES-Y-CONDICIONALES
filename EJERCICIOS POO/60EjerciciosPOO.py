# Solución ejercicio 63: Registro único por clave (simulando base simple)
class Repo:
    def __init__(self): self.storage={}
    def save(self,key,obj): self.storage[key]=obj
    def get(self,key): return self.storage.get(key)

if __name__ == '__main__':
    r = Repo(); r.save('a',1); print(r.get('a'))
