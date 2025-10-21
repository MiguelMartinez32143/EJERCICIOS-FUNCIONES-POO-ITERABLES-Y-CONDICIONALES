# Solución ejercicio 41: map con lambda
def map_lambda_ejemplo(lista):
    return list(map(lambda x: x*2, lista))

if __name__ == '__main__':
    print(map_lambda_ejemplo([1,2,3]))
