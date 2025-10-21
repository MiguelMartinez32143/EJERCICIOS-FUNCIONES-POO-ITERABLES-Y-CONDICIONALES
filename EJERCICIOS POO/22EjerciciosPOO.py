# Solución ejercicio 29: Serialización simple con pickle (guardar/leer objeto)
import pickle
class Demo: 
    def __init__(self,val): self.val=val

if __name__ == '__main__':
    d = Demo(10)
    path = '/mnt/data/demo_pickle.bin'
    with open(path,'wb') as f: pickle.dump(d,f)
    with open(path,'rb') as f: d2 = pickle.load(f)
    print(d2.val)
