# Solución ejercicio 19: closure contador
def crear_contador():
    n = 0
    def incrementar():
        nonlocal n
        n += 1
        return n
    return incrementar

if __name__ == '__main__':
    c = crear_contador()
    print(c(), c(), c())
