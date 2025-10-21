# Solución ejercicio 54: contar vocales en una cadena
def contar_vocales(s):
    return sum(1 for ch in s.lower() if ch in "aeiouáéíóú")

if __name__ == '__main__':
    print(contar_vocales("Hola"))
