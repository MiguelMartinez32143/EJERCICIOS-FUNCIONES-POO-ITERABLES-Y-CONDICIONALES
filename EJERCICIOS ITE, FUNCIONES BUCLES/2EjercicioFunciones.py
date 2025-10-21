# Solución ejercicio 10: mostrar info con argumentos nombrados
def mostrar_info(nombre, edad, ciudad):
    return f"{nombre} tiene {edad} años y vive en {ciudad}"

if __name__ == '__main__':
    print(mostrar_info(edad=25, ciudad="Medellín", nombre="Ana"))
