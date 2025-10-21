# Solución ejercicio 89: dividir lista en chunks de tamaño n
def chunks_of_size(lst,n):
    return [lst[i:i+n] for i in range(0,len(lst),n)]

if __name__ == '__main__':
    print(chunks_of_size([1,2,3,4,5],2))
