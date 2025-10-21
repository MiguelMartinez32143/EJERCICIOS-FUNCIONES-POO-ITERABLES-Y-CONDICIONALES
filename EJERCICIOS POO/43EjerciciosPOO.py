# Solución ejercicio 48: Mixin para representación JSON simple
import json
class JSONMixin:
    def to_json(self): return json.dumps(self.__dict__)
class User(JSONMixin):
    def __init__(self,n): self.name=n

if __name__ == '__main__':
    print(User('Ana').to_json())
