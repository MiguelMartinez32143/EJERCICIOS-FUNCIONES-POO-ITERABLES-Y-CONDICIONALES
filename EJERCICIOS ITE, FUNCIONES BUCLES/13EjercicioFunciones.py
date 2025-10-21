# Solución ejercicio 20: área de rectángulo con type hints y validación
def area_rectangulo(base: float, altura: float) -> float:
    """Calcula el área de un rectángulo."""
    if base < 0 or altura < 0:
        raise ValueError("Base y altura deben ser positivos")
    return base * altura

if __name__ == '__main__':
    print(area_rectangulo(3,4))
