# Solución ejercicio 87: escribir lista de líneas a archivo
def write_file_lines(path, lines):
    with open(path, "w", encoding="utf-8") as f:
        for l in lines:
            f.write(f"{l}\n")

if __name__ == '__main__':
    p = "/mnt/data/ejemplo_escritura.txt"
    write_file_lines(p, ["uno","dos"])
    print('Escrito', p)
