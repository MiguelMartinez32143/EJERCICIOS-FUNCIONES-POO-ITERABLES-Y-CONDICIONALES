# Solución ejercicio 45: Ejemplo de callback y observer simple
class Observador:
    def actualizar(self,msg): print('Recibido',msg)

class Sujeto:
    def __init__(self): self.obs = []
    def registrar(self,o): self.obs.append(o)
    def notificar(self,msg):
        for o in self.obs: o.actualizar(msg)

if __name__ == '__main__':
    s = Sujeto(); o = Observador(); s.registrar(o); s.notificar('Hola')
