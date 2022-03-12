"""
ASSOCIAÇAO - Usa | AGREGACAO - Tem | COMPOSIÇAO - É Dono | HERANÇA - É
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__

    def falar(self):
        print(f"{self.nomeclasse} está falando")


class Clientes(Pessoa):
    def comprar(self):
        print(f"{self.nomeclasse} está comprando")

    def falar(self):
        print(f"{self.nomeclasse} está falando sobre negócios")


class Aluno(Pessoa):
    def estudar(self):
        print(f"{self.nomeclasse} está estudando")


class ClienteVIP(Clientes):  # Herda de cliente, que tbm herda de pessoa, logo ClienteVIP tbm herda de pessoa
    def falar(self):
        Pessoa.falar(self)
        super().falar()  # Vai execultar o metodo falar primeiro da super classe acima dessa classe
        print(f"{self.nome} {self.sobrenome} está falando como é bom ser vip")  # Estou sobrepondo o metodo falar em outra class

    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)  # Com o super, não passa o self como parametro. Se for sobrepor pelo nome da classe, usa-se self
        self.sobrenome = sobrenome


c1 = Clientes("Luiz", 45)
c2 = ClienteVIP("Rose", 25, "Souza")
print(c1.nomeclasse, c1.nome)
a1 = Aluno("Igor", 18)
print(a1.nomeclasse, a1.nome)
print()
c2.falar()
print()
c1.comprar()
c2.comprar()
