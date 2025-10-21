# Solución ejercicio 15: Uso de propiedades (getter/setter) con validación
class Persona:
    def __init__(self,nombre,edad):
        self.__nombre = nombre; self.__edad = edad
    @property
    def edad(self): return self.__edad
    @edad.setter
    def edad(self,val):
        if 0<=val<=150: self.__edad = val
        else: raise ValueError('Edad inválida')

if __name__ == '__main__':
    p = Persona('Ana',25); p.edad = 26; print(p.edad)
