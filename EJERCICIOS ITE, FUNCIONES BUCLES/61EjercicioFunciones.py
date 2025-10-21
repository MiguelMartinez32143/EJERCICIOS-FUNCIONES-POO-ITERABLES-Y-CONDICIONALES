# Solución ejercicio 64: primalidad simple
def es_primo(n):
    if n<2: return False
    i=2
    while i*i<=n:
        if n%i==0: return False
        i+=1
    return True

if __name__ == '__main__':
    print(es_primo(17))
