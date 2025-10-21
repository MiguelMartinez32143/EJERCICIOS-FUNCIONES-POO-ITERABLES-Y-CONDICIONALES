# Solución ejercicio 65: Clase con método estático utilitario (formato)
class Utils:
    @staticmethod
    def es_par(n): return n%2==0

if __name__ == '__main__':
    print(Utils.es_par(4))
