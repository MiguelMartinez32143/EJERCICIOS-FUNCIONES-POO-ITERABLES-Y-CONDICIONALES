# Solución ejercicio 72: Decorador de clase que añade atributo extra a la clase
def add_version(v):
    def deco(cls):
        cls.version = v; return cls
    return deco

@add_version('1.0')
class A: pass

if __name__ == '__main__':
    print(A.version)
