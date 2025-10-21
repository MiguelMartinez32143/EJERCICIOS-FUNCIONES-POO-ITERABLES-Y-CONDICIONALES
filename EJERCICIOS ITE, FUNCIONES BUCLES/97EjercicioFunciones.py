# Solución ejercicio 97: longitud media de palabras en texto
def palabras_longitud_media(text):
    words = text.split()
    if not words: return 0
    return sum(len(w) for w in words)/len(words)

if __name__ == '__main__':
    print(palabras_longitud_media("hola mundo claro"))
