# Solución ejercicio 88: conversión segura a int con default
def safe_int(x, default=0):
    try:
        return int(x)
    except Exception:
        return default

if __name__ == '__main__':
    print(safe_int("5"))
    print(safe_int("a", -1))
