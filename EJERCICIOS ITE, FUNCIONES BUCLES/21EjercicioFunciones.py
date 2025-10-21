# Solución ejercicio 28: buscar en diccionario con get
def buscar(dic, nombre):
    return dic.get(nombre)

if __name__ == '__main__':
    alumnos = {"Ana":9, "Luis":7}
    print(buscar(alumnos, "Ana"))
    print(buscar(alumnos, "X"))
