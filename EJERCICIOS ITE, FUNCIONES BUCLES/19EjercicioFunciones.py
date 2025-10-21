# Solución ejercicio 26: evitar mutable por defecto
def agregar_bien(item, lista=None):
    if lista is None:
        lista = []
    lista.append(item)
    return lista

if __name__ == '__main__':
    print(agregar_bien(1))
    print(agregar_bien(2))
