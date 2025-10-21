# Solución ejercicio 31: filtrar por nota mínima
def filtrar_por_nota(dic, minimo):
    return {k:v for k,v in dic.items() if v >= minimo}

if __name__ == '__main__':
    print(filtrar_por_nota({"A":5,"B":8},6))
