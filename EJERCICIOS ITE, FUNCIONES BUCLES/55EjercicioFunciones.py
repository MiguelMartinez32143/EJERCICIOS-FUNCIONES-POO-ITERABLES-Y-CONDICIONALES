# Solución ejercicio 59: aplanar lista de listas
def flatten(ll):
    return [x for sub in ll for x in sub]

if __name__ == '__main__':
    print(flatten([[1,2],[3,4]]))
