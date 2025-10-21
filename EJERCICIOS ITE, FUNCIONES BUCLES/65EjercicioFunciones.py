# Solución ejercicio 68: máximo común divisor (Euclides)
def gcd(a,b):
    while b:
        a,b = b, a%b
    return abs(a)

if __name__ == '__main__':
    print(gcd(48,18))
