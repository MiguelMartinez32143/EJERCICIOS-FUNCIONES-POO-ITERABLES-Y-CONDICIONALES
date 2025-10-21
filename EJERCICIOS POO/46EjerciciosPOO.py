# Solución ejercicio 50: Uso de weakref para evitar referencias fuertes (demostración)
import weakref
class A: pass
if __name__ == '__main__':
    a = A(); wr = weakref.ref(a)
    print(wr()); del a
    print(wr())
