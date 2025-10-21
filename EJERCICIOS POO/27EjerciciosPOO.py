# Solución ejercicio 33: Singleton (implementación simple por clase)
class Singleton:
    _inst = None
    def __new__(cls,*a,**k):
        if cls._inst is None: cls._inst = super().__new__(cls)
        return cls._inst

if __name__ == '__main__':
    a = Singleton(); b = Singleton(); print(a is b)
