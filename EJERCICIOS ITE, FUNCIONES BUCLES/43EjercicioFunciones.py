# Solución ejercicio 48: closure sumador
def closure_sumador(x):
    def sumar(y):
        return x + y
    return sumar

if __name__ == '__main__':
    add5 = closure_sumador(5)
    print(add5(3))
