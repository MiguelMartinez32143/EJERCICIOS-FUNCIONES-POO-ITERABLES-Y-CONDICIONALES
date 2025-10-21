# Solución ejercicio 65: lista de primos hasta n
def lista_primos_hasta(n):
    return [i for i in range(2,n+1) if es_primo(i)]

if __name__ == '__main__':
    print(lista_primos_hasta(20))
