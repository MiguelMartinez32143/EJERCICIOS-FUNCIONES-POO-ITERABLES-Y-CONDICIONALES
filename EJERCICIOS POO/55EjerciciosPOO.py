# Solución ejercicio 59: Ejemplo simple de EventEmitter (suscribir y emitir eventos)
class Emitter:
    def __init__(self): self.handlers = []
    def on(self,h): self.handlers.append(h)
    def emit(self,*a,**k):
        for h in self.handlers: h(*a,**k)

if __name__ == '__main__':
    e = Emitter(); e.on(lambda x: print('Recibido',x)); e.emit('Hola')
