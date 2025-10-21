# Solución ejercicio 64: Clase que valida formato (ej. email) en setter
import re
class Usuario:
    def __init__(self,email): self.email=email
    @property
    def email(self): return self._email
    @email.setter
    def email(self,v):
        if not re.match(r'[^@]+@[^@]+\.[^@]+', v): raise ValueError('Email inválido')
        self._email = v

if __name__ == '__main__':
    try: Usuario('x'); except Exception as e: print('Invalid:', e)
