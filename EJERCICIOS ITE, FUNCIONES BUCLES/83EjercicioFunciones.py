# Solución ejercicio 84: aplanar una sola profundidad
def flatten_once(lst):
    res=[]
    for x in lst:
        if isinstance(x, list):
            res.extend(x)
        else:
            res.append(x)
    return res

if __name__ == '__main__':
    print(flatten_once([1,[2,3],4]))
