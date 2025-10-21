# Solución ejercicio 2: Clase Calculadora con operaciones básicas
class Calculadora:
    def sumar(self,a,b): return a+b
    def restar(self,a,b): return a-b
    def multiplicar(self,a,b): return a*b
    def dividir(self,a,b):
        if b==0: return 'Error: División por cero'
        return a/b

if __name__ == '__main__':
    c = Calculadora()
    print(c.sumar(5,3))
    print(c.dividir(10,0))
