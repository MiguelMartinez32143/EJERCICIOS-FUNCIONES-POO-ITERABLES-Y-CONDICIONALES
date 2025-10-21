# Solución ejercicio 98: agrupar por función (group_by)
from collections import defaultdict
def group_by(func, it):
    d=defaultdict(list)
    for x in it:
        d[func(x)].append(x)
    return dict(d)

if __name__ == '__main__':
    print(group_by(lambda x: x%2, [1,2,3,4]))
