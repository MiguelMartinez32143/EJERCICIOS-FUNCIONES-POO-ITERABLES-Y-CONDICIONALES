# Solución ejercicio 30: modificar nota si existe
def modificar_nota(dic, nombre, nueva):
    if nombre in dic:
        dic[nombre] = nueva
        return True
    return False

if __name__ == '__main__':
    d = {"Ana":9}
    print(modificar_nota(d,"Ana",8), d)
