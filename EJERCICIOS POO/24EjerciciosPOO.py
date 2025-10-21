# Solución ejercicio 30: Context manager simple con __enter__/__exit__
class Recurso:
    def __enter__(self): print('Entrando'); return self
    def __exit__(self,exc_type,exc,trace): print('Saliendo'); return False

if __name__ == '__main__':
    with Recurso() as r:
        print('Dentro')
