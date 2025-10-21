# Solución ejercicio 53: palíndromo (ignora caracteres no alfanuméricos)
def palindromo(s):
    s2 = ''.join(ch.lower() for ch in s if ch.isalnum())
    return s2 == s2[::-1]

if __name__ == '__main__':
    print(palindromo("A man, a plan, a canal"))
