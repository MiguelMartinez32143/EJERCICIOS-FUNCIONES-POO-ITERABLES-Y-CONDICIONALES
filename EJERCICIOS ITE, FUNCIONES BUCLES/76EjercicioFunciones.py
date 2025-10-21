# Solución ejercicio 78: cuenta regresiva recursiva
def countdown(n):
    if n <= 0:
        print("BOOM")
        return
    print(n)
    countdown(n-1)

if __name__ == '__main__':
    countdown(3)
