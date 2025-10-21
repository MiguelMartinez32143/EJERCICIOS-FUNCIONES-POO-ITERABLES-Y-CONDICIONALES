# Solución ejercicio 91: Clase con documentación (docstrings) y help demonstration
class Demo:
    """Demo: clase de ejemplo con docstring"""
    def metodo(self):
        """Hace algo"""
        return True

if __name__ == '__main__':
    print(Demo.__doc__); print(Demo.metodo.__doc__)
