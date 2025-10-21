# Solución ejercicio 83: Clase que implementa estrategia (Strategy pattern)
class EstrategiaA:
    def ejecutar(self): return 'A'
class EstrategiaB:
    def ejecutar(self): return 'B'
class Contexto:
    def __init__(self,estrat): self.estrat = estrat
    def run(self): return self.estrat.ejecutar()

if __name__ == '__main__':
    print(Contexto(EstrategiaA()).run(), Contexto(EstrategiaB()).run())
