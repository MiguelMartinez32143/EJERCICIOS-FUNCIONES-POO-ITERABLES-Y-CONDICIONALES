# Solución ejercicio 96: dividir 100 por cada elemento, manejar división por cero
def safe_divide_list(lst):
    res=[]
    for v in lst:
        res.append(None if v==0 else 100/v)
    return res

if __name__ == '__main__':
    print(safe_divide_list([25,0,4]))
