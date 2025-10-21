# Solución ejercicio 24: Duck Typing - función que llama a .nadar() y .hacer_sonido()
class Pato: 
    def nadar(self): return 'Pato nadando'
    def hacer_sonido(self): return 'Cuac'
class Persona:
    def nadar(self): return 'Persona nadando'
    def hacer_sonido(self): return 'Hola'

def actividad(p):
    print(p.nadar()); print(p.hacer_sonido())

if __name__ == '__main__':
    actividad(Pato()); actividad(Persona())
