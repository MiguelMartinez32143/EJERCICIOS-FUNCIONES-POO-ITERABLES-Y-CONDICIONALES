# Solución ejercicio 37: Métodos privados (convención) y públicos que los usan
class Clase:
    def __init__(self): self._valor = 0
    def _privado(self): return 'privado'
    def publico(self): return self._privado()

if __name__ == '__main__':
    print(Clase().publico())
