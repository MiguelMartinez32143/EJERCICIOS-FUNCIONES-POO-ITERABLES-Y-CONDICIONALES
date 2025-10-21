# Solución ejercicio 21: ordenar por longitud usando lambda
def ordenar_por_longitud(palabras):
    return sorted(palabras, key=lambda p: len(p))

if __name__ == '__main__':
    print(ordenar_por_longitud(["python","es","genial"]))
