# Solución ejercicio 76: Clase que implementa método estático factory
class Logger:
    @staticmethod
    def default(): return Logger()

if __name__ == '__main__':
    print(isinstance(Logger.default(), Logger))
