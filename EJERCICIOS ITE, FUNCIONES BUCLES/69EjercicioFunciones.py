# Solución ejercicio 71: dividir string en chunks de tamaño k
def split_chunks(s,k):
    return [s[i:i+k] for i in range(0,len(s),k)]

if __name__ == '__main__':
    print(split_chunks("abcdefgh",3))
