# Solución ejercicio 85: elemento más frecuente (Counter)
def most_common(lst):
    from collections import Counter
    if not lst: return None
    return Counter(lst).most_common(1)[0][0]

if __name__ == '__main__':
    print(most_common([1,2,2,3]))
