# Solución ejercicio 69: mínimo común múltiplo usando gcd
def lcm(a,b):
    return abs(a*b)//gcd(a,b) if a and b else 0

if __name__ == '__main__':
    print(lcm(4,6))
