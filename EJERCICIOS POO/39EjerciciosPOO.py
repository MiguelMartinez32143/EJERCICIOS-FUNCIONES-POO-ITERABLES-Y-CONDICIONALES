# Solución ejercicio 44: Uso de metaclases simple para rastrear clases creadas
class Meta(type):
    clases = []
    def __new__(mcls,name,bases,ns):
        cls = super().__new__(mcls,name,bases,ns)
        Meta.clases.append(name)
        return cls

class A(metaclass=Meta): pass
class B(metaclass=Meta): pass

if __name__ == '__main__':
    print(Meta.clases)
