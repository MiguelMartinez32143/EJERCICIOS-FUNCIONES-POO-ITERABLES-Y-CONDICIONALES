# Solución ejercicio 35: Validación en constructor y raising de excepciones
class Rect:
    def __init__(self,l,a):
        if l<=0 or a<=0: raise ValueError('Dimensiones invalidas')
        self.l = l; self.a = a

if __name__ == '__main__':
    try:
        r = Rect(-1,2)
    except Exception as e:
        print('Error capturado:', e)
