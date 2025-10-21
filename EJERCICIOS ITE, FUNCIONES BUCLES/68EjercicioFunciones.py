# Solución ejercicio 70: ordenar diccionario por valor (desc)
def ordenar_dic_por_valor(dic):
    return sorted(dic.items(), key=lambda kv: kv[1], reverse=True)

if __name__ == '__main__':
    print(ordenar_dic_por_valor({'a':2,'b':5}))
