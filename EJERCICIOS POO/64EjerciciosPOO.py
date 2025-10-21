# Solución ejercicio 67: Clase que implementa búsqueda binaria sobre lista de objetos por atributo
class Obj: 
    def __init__(self,val): self.val=val
def binary_search_objs(arr, x):
    lo,hi=0,len(arr)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if arr[mid].val==x: return mid
        if arr[mid].val<x: lo=mid+1
        else: hi=mid-1
    return -1

if __name__ == '__main__':
    arr=[Obj(i) for i in range(0,10)]; print(binary_search_objs(arr,7))
