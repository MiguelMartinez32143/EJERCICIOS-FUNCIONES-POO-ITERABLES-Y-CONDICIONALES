# Solución ejercicio 55: comprobar anagramas
def es_anagrama(a,b):
    return sorted(a.replace(" ","").lower()) == sorted(b.replace(" ","").lower())

if __name__ == '__main__':
    print(es_anagrama("roma","amor"))
