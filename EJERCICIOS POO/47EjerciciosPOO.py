# Solución ejercicio 51: Manejo básico de excepciones dentro de métodos
class Div:
    def dividir(self,a,b):
        try: return a/b
        except ZeroDivisionError: return None

if __name__ == '__main__':
    print(Div().dividir(10,0))
