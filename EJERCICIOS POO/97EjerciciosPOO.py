# Solución ejercicio 97: Clase que implementa retry decorator a nivel de método
import functools, time
def retry(tries=3):
    def deco(fn):
        @functools.wraps(fn)
        def wrapper(*a,**k):
            for i in range(tries):
                try: return fn(*a,**k)
                except Exception:
                    if i==tries-1: raise
                    time.sleep(0.01)
        return wrapper
    return deco

class Demo:
    @retry(2)
    def run(self): return 'ok'

if __name__ == '__main__':
    print(Demo().run())
