# Solución ejercicio 33: guardar diccionario a archivo CSV simple
def guardar_txt(dic, nombre_archivo):
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        for k,v in dic.items():
            f.write(f"{k},{v}\n")

if __name__ == '__main__':
    guardar_txt({"Ana":9,"Luis":7}, "/mnt/data/alumnos_ejemplo.txt")
    print('Archivo creado en /mnt/data/alumnos_ejemplo.txt')
