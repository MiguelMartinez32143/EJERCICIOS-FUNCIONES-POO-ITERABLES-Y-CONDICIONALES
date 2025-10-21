# Solución ejercicio 80: convertir a Title Case
def to_title_case(s):
    return ' '.join(w.capitalize() for w in s.split())

if __name__ == '__main__':
    print(to_title_case("hola mundo"))
