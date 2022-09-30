from abc import ABC, abstractmethod


class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.conta = []

    def inserir_cliente(self,cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.conta.append(conta)

    def autenticar(self, cliente):
        if cliente not in self.clientes:
            return False

        if cliente.conta not in self.conta:
            return False

        if cliente.conta.agencia not in self.agencias:
            return False

        return True

class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @property
    def idade(self):
        return self._idade


class Cliente(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.conta = None

    def inserir_conta(self, conta):
        self.conta = conta


class Conta(ABC):
    def __init__(self, agencia, numero, saldo):
        self.agencia = agencia
        self.numero = numero
        self.saldo = saldo

    @abstractmethod
    def sacar(self, sub):
        pass

    def consultarSaldo(self):
        print(self.saldo)

    def depositar(self, soma):
        self.saldo += soma
        self.consultarSaldo()


class ContaCorrente(Conta):
    def __init__(self, agencia, numero, saldo, limite=100):
        super().__init__(agencia, numero, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < valor:
            print("Saldo insuficiente")
            return

        self.saldo -= valor
        self.consultarSaldo()


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self.saldo < valor:
            print("Saldo insuficiente")
            return

        self.saldo -= valor
        self.consultarSaldo()



banco = Banco()
cliente1 = Cliente("Luiz", 30)
cliente2 = Cliente("Maria", 20)
cliente3 = Cliente("Jeni", 19)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0)
conta3 = ContaPoupanca(1212, 254138, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)


if banco.autenticar(cliente1):
    cliente1.conta.depositar(40)
    cliente1.conta.sacar(20)
else:
    print("Cliente não autenticado")
if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print("Cliente não autenticado")

