# Solución ejercicio 66: convertir a binario (string)
def convertir_binario(n):
    return bin(n)[2:]

if __name__ == '__main__':
    print(convertir_binario(10))
