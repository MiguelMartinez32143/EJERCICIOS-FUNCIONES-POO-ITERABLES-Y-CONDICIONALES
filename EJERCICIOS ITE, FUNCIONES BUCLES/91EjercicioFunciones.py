# Solución ejercicio 91: validación simple de email (regex)
import re
def is_valid_email(s):
    return re.match(r"[^@]+@[^@]+\.[^@]+", s) is not None

if __name__ == '__main__':
    print(is_valid_email("test@example.com"))
