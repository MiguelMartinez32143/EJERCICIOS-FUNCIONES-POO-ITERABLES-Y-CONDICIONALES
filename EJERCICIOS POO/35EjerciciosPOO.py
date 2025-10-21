# Solución ejercicio 40: Polimorfismo en sistema de pagos (clases y procesador)
class MetodoPago:
    def __init__(self,monto): self.monto=monto
    def procesar(self): raise NotImplementedError
class Efectivo(MetodoPago):
    def procesar(self): return f'Efectivo ${self.monto}'
class Tarjeta(MetodoPago):
    def procesar(self): return f'Tarjeta ${self.monto}'

if __name__ == '__main__':
    for m in [Efectivo(50), Tarjeta(100)]: print(m.procesar())
