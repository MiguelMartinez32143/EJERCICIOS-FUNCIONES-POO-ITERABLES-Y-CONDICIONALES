# Solución ejercicio 27: encontrar max, min y promedio
def encontrar_max_min(lista):
    if not lista: return None, None, None
    return max(lista), min(lista), sum(lista)/len(lista)

if __name__ == '__main__':
    print(encontrar_max_min([1,2,3,4]))
