# Solución ejercicio 38: Uso de super() para extender comportamiento del padre
class A:
    def saludar(self): return 'Hola A'
class B(A):
    def saludar(self): return super().saludar() + ' y B'

if __name__ == '__main__':
    print(B().saludar())
