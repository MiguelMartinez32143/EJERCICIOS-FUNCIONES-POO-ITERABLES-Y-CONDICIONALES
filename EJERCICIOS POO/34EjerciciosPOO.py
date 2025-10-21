# Solución ejercicio 3: CuentaBancaria con depositar, retirar y consultar saldo
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # privado

    def depositar(self,cantidad):
        if cantidad>0:
            self.__saldo += cantidad
            return f"✓ Depositado: ${cantidad}. Saldo: ${self.__saldo}"
        return 'Cantidad inválida'

    def retirar(self,cantidad):
        if cantidad>self.__saldo: return 'Fondos insuficientes'
        self.__saldo -= cantidad
        return f"✓ Retirado: ${cantidad}. Saldo: ${self.__saldo}"

    def consultar_saldo(self):
        return self.__saldo

if __name__ == '__main__':
    acc = CuentaBancaria('Juan', 1000)
    print(acc.depositar(500))
    print(acc.retirar(200))
    print(acc.consultar_saldo())
