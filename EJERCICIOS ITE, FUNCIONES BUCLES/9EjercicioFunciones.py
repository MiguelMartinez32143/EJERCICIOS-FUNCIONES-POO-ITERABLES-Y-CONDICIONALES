# Solución ejercicio 17: función flexible con *args y **kwargs
def funcion_flexible(*args, **kwargs):
    return {"args": args, "kwargs": kwargs}

if __name__ == '__main__':
    print(funcion_flexible(1,2, nombre="Ana"))
