# Solución ejercicio 86: leer archivo y devolver líneas (strip)
def read_file_lines(path):
    with open(path, encoding="utf-8") as f:
        return [line.rstrip("\n") for line in f]

if __name__ == '__main__':
    p = "/mnt/data/ejemplo_lectura.txt"
    with open(p, 'w', encoding='utf-8') as f:
        f.write("line1\nline2\n")
    print(read_file_lines(p))
