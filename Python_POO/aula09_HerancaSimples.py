"""
ASSOCIAÇAO - Usa | AGREGACAO - Tem | COMPOSIÇAO - É Dono | HERANÇA - É
"""


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeclasse = self.__class__.__name__


class Clientes(Pessoa):
    pass


class Aluno(Pessoa):
    pass

c1 = Clientes("Luiz", 45)
print(c1.nomeclasse, c1.nome)
a1 = Aluno("Igor", 18)
print(a1.nomeclasse, a1.nome)
