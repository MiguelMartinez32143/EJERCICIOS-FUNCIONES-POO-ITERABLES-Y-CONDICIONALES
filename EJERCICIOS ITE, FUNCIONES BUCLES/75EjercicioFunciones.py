# Solución ejercicio 77: merge sort recursivo
def merge_sort(lst):
    if len(lst) <= 1: return lst
    mid = len(lst)//2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    i,j=0,0; res=[]
    while i<len(left) and j<len(right):
        if left[i] <= right[j]:
            res.append(left[i]); i+=1
        else:
            res.append(right[j]); j+=1
    res.extend(left[i:]); res.extend(right[j:])
    return res

if __name__ == '__main__':
    print(merge_sort([5,2,9,1]))
