# Solución ejercicio 27: Uso de dataclasses para clases sencillas
from dataclasses import dataclass
@dataclass
class Producto:
    nombre: str
    precio: float
    stock: int = 0

if __name__ == '__main__':
    p = Producto('Mesa', 120.5, 3); print(p)
