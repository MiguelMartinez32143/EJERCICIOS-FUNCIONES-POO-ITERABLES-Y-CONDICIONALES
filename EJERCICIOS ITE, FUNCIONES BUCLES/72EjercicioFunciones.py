# Solución ejercicio 74: comprobar si lista está ordenada non-decreasing
def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

if __name__ == '__main__':
    print(is_sorted([1,2,2,3]))
