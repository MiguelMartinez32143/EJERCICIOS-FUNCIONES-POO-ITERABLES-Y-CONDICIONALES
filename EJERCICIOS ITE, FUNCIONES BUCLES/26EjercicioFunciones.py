# Solución ejercicio 32: estadísticas básicas de diccionario de notas
def estadisticas(dic):
    if not dic: return {"total":0}
    notas = list(dic.values())
    return {
        "total": len(notas),
        "max": max(notas),
        "min": min(notas),
        "promedio": sum(notas)/len(notas)
    }

if __name__ == '__main__':
    print(estadisticas({"A":9,"B":7}))
