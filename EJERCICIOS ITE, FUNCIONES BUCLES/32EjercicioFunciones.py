# Solución ejercicio 38: ejemplo con variable global correctamente usada
total = 0
def agregar(valor):
    global total
    total += valor
    return total

if __name__ == '__main__':
    print(agregar(5))
    print(agregar(3))
