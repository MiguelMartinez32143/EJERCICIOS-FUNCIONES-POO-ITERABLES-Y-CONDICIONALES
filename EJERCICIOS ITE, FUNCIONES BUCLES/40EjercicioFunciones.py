# Solución ejercicio 45: print vs return
def f_print():
    print("hola")

def f_return():
    return "hola"

if __name__ == '__main__':
    x = f_print()
    y = f_return()
    print(x, y)
