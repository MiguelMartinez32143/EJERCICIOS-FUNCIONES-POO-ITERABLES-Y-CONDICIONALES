# Solución ejercicio 93: normalizar espacios extra
def normalize_spaces(s):
    return ' '.join(s.split())

if __name__ == '__main__':
    print(normalize_spaces("  hola   mundo  "))
