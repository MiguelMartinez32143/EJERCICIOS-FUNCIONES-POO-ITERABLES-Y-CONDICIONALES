# Solución ejercicio 81: comprobar caracteres únicos
def unique_chars(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    print(unique_chars("abc"))
    print(unique_chars("aba"))
