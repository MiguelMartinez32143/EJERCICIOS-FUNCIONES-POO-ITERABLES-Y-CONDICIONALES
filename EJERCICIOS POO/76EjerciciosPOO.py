# Solución ejercicio 78: Clase que valida en __post_init__ (con dataclass)
from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int

    def __post_init__(self):
        if self.age < 0: raise ValueError('Edad negativa')

if __name__ == '__main__':
    print(User('Ana',25))
