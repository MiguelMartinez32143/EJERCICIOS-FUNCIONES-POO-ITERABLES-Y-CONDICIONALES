# Solución ejercicio 84: Pruebas simples (assert) dentro de __main__ como sanity checks
class Calc: 
    def add(self,a,b): return a+b

if __name__ == '__main__':
    c = Calc(); assert c.add(2,3)==5; print('Tests simples OK')
