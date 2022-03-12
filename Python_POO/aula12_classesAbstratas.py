"""
CLASSES ABSTRATAS - CoNcEiToS - você está basicamente informando que esse método não foi implementado ainda e que
 precisa ser implementado nas subclasses. Ele é bastante usado em abstrações em geral e padrões de projeto
"""
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self):
        pass


class B(A):
    def falar(self):
        print("Falando...")


a = B()
a.falar()
# a = A()  # Isso dá erro, pois está instanciando uma classe abstrata

# EXEMPLO


class Banco(ABC):
    def __init__(self, agentcia, conta, saldo):
        self._agencia = agentcia
        self._conta = conta
        self._saldo = saldo

    @property
    def agencia(self):
        return self._agencia

    @property
    def conta(self):
        return self._conta

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Saldo precisa ser numérico")

        self._saldo = valor

    def depositar(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("Valor do depósito precisa ser numérico")

        self.saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f"Agência: {self.agencia}", end=" ")
        print(f"Conta: {self.conta}", end=" ")
        print(f"Saldo: {self.saldo}")

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaPoupanca(Banco):
    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente')
            self.detalhes()
            return
        self.saldo -= valor
        self.detalhes()


class ContaCorrente(Banco):
    def __init__(self, agencia, conta, saldo, limite = 100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    @property
    def limite(self):
        return self._limite



    def sacar(self, valor):
        if (self.limite + self.saldo) < valor:
            print('Saldo insuficiente')
            self.detalhes()
            return
        self.saldo -= valor
        self.detalhes()

cp = ContaPoupanca(1111, 2222, 0)
cp.depositar(10)
cp.depositar(80)
cp.sacar(50)
cp.sacar(50)
print("########")

cc = ContaCorrente(1111, 3333, 0, 500)
cc. depositar(800)
cc.sacar(900)
cc.sacar(500)
