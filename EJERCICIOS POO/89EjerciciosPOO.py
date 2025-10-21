# Solución ejercicio 8: Empleado con salario y aplicación de aumentos
class Empleado:
    def __init__(self,nombre, puesto, salario_mensual):
        self.nombre = nombre
        self.puesto = puesto
        self.salario_mensual = salario_mensual

    def salario_anual(self): return self.salario_mensual * 12

    def aplicar_aumento(self, porcentaje):
        if porcentaje<=0: return 'Porcentaje inválido'
        self.salario_mensual *= 1 + porcentaje/100
        return self.salario_mensual

if __name__ == '__main__':
    emp = Empleado('Carlos','Dev',3000)
    print(emp.salario_anual()); print(emp.aplicar_aumento(10))
