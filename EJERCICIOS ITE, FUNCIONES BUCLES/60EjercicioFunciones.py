# Solución ejercicio 63: convertir a camelCase
def to_camel_case(s):
    parts = s.split()
    return parts[0].lower() + ''.join(p.capitalize() for p in parts[1:])

if __name__ == '__main__':
    print(to_camel_case("hola mundo prueba"))
