# Solución ejercicio 34: sistema de plugins simple con decorador
PLUGINS = {}

def plugin(nombre):
    def decorador(func):
        PLUGINS[nombre] = func
        return func
    return decorador

@plugin("hola")
def p_hola(): return "hola plugin"

def ejecutar(nombre, *args, **kwargs):
    func = PLUGINS.get(nombre)
    if not func:
        return f"Plugin {nombre} no existe"
    return func(*args, **kwargs)

if __name__ == '__main__':
    print(ejecutar("hola"))
