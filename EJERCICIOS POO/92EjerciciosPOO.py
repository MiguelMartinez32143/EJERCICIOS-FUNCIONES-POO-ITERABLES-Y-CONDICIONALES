# Solución ejercicio 92: Clase que exporta e importa JSON de su estado
import json
class Config:
    def __init__(self, **kwargs): self.__dict__.update(kwargs)
    def save(self,path): open(path,'w').write(json.dumps(self.__dict__))
    @classmethod
    def load(cls,path): return cls(**json.loads(open(path).read()))

if __name__ == '__main__':
    c = Config(a=1); c.save('/mnt/data/config.json'); print(Config.load('/mnt/data/config.json').a)
