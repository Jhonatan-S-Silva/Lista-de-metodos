class ContaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial  # Atributo "protegido"

    @property
    def saldo(self):
        return self._saldo  # Somente leitura

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor):
        if 0 < valor <= self._saldo:
            self._saldo -= valor

conta = ContaBancaria(1000)
print(conta.saldo)  

conta.depositar(500)
print(conta.saldo)  

conta.sacar(200)
print(conta.saldo) 