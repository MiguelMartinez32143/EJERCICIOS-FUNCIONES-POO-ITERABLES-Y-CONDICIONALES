# Solución ejercicio 90: transpone una matriz (lista de listas)
def transpose(matrix):
    return list(map(list, zip(*matrix)))

if __name__ == '__main__':
    print(transpose([[1,2,3],[4,5,6]]))
