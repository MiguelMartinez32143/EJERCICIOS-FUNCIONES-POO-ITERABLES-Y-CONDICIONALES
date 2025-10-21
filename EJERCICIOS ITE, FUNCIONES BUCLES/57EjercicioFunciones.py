# Solución ejercicio 60: contar ocurrencias en lista
def contar_ocurrencias(lista):
    d={}
    for x in lista:
        d[x]=d.get(x,0)+1
    return d

if __name__ == '__main__':
    print(contar_ocurrencias([1,2,2,3]))
