# Solución ejercicio 94: obtener extensión de archivo
def get_file_extension(fn):
    idx = fn.rfind('.')
    return fn[idx+1:] if idx!=-1 else ''

if __name__ == '__main__':
    print(get_file_extension("doc.pdf"))
