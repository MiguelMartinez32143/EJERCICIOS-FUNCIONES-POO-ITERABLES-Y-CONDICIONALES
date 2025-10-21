# Solución ejercicio 5: Producto de tienda con stock y cálculo de valor
class Producto:
    def __init__(self,nombre,precio,stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        return f"{self.nombre} - ${self.precio:.2f} - Stock: {self.stock}"

    def actualizar_stock(self,c):
        self.stock += c
        return self.stock

    def calcular_valor_total(self, unidades):
        if unidades<=0: return 'Cantidad inválida'
        if unidades>self.stock: return 'Stock insuficiente'
        return unidades * self.precio

if __name__ == '__main__':
    p = Producto('Laptop',1200,10)
    print(p.mostrar_info())
    print(p.calcular_valor_total(3))
