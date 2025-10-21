# Solución ejercicio 82: rotar lista a la derecha k posiciones
def rotate_list(lst,k):
    if not lst: return lst
    k %= len(lst)
    return lst[-k:] + lst[:-k]

if __name__ == '__main__':
    print(rotate_list([1,2,3,4],1))
