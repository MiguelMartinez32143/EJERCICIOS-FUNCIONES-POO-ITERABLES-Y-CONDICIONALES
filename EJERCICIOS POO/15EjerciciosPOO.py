# Solución ejercicio 22: Notificador abstracto con implementaciones concretas
from abc import ABC, abstractmethod
class Notificador(ABC):
    @abstractmethod
    def enviar(self,dest,msg): pass

class Email(Notificador):
    def enviar(self,dest,msg): return f"Email a {dest}: {msg}"

if __name__ == '__main__':
    n = Email(); print(n.enviar('x@y.com','Hola'))
