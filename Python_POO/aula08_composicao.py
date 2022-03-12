class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.endereco = []

    def insere_endereco(self, cidade, estado):
        self.endereco.append(Endereco(cidade, estado))

    def lista_endereco(self):
        for endereco in self.endereco:
            print(endereco.cidade, endereco.estado)


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self. estado = estado


cliente1 = Cliente("LUIZ", 32)
print(cliente1.nome)
cliente1.insere_endereco("Salvador", "BA")
cliente1.lista_endereco()
print()

cliente2 = Cliente("Maria", 50)
print(cliente2.nome)
cliente2.insere_endereco("Guarulhos", "SP")
cliente2.lista_endereco()
print()
