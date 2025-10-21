# Solución ejercicio 72: cifrado rot13 usando codecs
import codecs
def rot13(s):
    return codecs.decode(s, "rot_13")

if __name__ == '__main__':
    print(rot13("uryyb"))
