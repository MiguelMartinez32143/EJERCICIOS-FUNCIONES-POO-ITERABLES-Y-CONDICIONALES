# Solución ejercicio 56: contar palabras
def contar_palabras(s):
    words = s.lower().split()
    d = {}
    for w in words:
        d[w] = d.get(w,0)+1
    return d

if __name__ == '__main__':
    print(contar_palabras("hola hola mundo"))
