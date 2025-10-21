# Solución ejercicio 100: sistema simplificado de alumnos (pequeña API interna)
def sistema_alumnos_cli():
    alumnos = {}
    def agregar(nombre, nota): alumnos[nombre]=nota
    def mostrar(): return alumnos.copy()
    def mejor():
        if not alumnos: return None
        return max(alumnos.items(), key=lambda kv: kv[1])
    return {"agregar":agregar, "mostrar":mostrar, "mejor":mejor}

if __name__ == '__main__':
    s = sistema_alumnos_cli()
    s['agregar']("Ana",9); s['agregar']("Luis",7)
    print(s['mostrar']())
    print(s['mejor']())
