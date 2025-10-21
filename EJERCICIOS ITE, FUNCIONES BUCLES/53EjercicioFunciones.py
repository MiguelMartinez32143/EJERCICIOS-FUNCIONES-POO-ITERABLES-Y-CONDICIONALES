# Solución ejercicio 57: eliminar duplicados preservando orden
def lista_unica(lst):
    seen = set()
    res = []
    for x in lst:
        if x not in seen:
            seen.add(x)
            res.append(x)
    return res

if __name__ == '__main__':
    print(lista_unica([1,2,2,3,1]))
