# Solución ejercicio 29: eliminar llave de diccionario
def eliminar(dic, nombre):
    return dic.pop(nombre, None) is not None

if __name__ == '__main__':
    d = {"Ana":9}
    print(eliminar(d,"Ana"), d)
