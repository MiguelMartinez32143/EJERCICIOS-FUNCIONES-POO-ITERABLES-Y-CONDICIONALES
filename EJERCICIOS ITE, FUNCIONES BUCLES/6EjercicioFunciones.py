# Solución ejercicio 14: fibonacci recursivo
def fibonacci_rec(n):
    if n < 2:
        return n
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

if __name__ == '__main__':
    print([fibonacci_rec(i) for i in range(8)])
