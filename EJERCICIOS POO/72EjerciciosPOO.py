# Solución ejercicio 74: Clase que expone API mínima y oculta implementación (abstracción)
class Calculadora:
    def sumar(self,a,b): return a+b
    def _log(self,msg): pass  # detalle oculto

if __name__ == '__main__':
    print(Calculadora().sumar(2,3))
