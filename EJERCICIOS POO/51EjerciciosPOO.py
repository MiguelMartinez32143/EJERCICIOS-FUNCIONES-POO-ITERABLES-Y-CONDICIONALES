# Solución ejercicio 55: Clase que registra historial de cambios (pattern Memento simple)
class Documento:
    def __init__(self, texto=''): self.texto = texto; self.hist = []
    def guardar(self): self.hist.append(self.texto)
    def restaurar(self, idx): self.texto = self.hist[idx]

if __name__ == '__main__':
    d = Documento('v1'); d.guardar(); d.texto='v2'; d.guardar(); d.restaurar(0); print(d.texto)
