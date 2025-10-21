# Solución ejercicio 51: validar que la entrada es número (float)
def validar_entrada_numero(x):
    try:
        return float(x)
    except Exception:
        raise ValueError("No es un número válido")

if __name__ == '__main__':
    print(validar_entrada_numero("3.5"))
