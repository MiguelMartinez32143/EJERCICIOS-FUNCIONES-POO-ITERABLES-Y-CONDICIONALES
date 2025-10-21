# Solución ejercicio 95: unica preservando orden (similar a lista_unica)
def unique_preserve_order(seq):
    seen=set(); out=[]
    for x in seq:
        if x not in seen:
            seen.add(x); out.append(x)
    return out

if __name__ == '__main__':
    print(unique_preserve_order([3,1,3,2]))
