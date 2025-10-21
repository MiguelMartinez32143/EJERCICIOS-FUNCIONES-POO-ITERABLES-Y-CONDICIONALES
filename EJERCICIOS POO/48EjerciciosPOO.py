# Solución ejercicio 52: Implementar un registro (logger) simple dentro de una clase
class Logger:
    def __init__(self): self.logs = []
    def info(self,msg): self.logs.append(('INFO',msg))
    def mostrar(self): return self.logs

if __name__ == '__main__':
    L = Logger(); L.info('inicio'); print(L.mostrar())
