class Carrinho:
    def __init__(self):
        self.produto = []

    def inserir_produto(self, produto):
        self.produto.append(produto)

    def lista_produto(self):
        for produto in self.produto:
            print(produto.nome, produto.valor)

    def soma_total(self):
        total = 0
        for produto in self.produto:
            total += produto.valor
        return total

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor




carrinho = Carrinho()
p1 = Produto("camiseta", 50)
p2 = Produto("Calça", 80)
p3 = Produto("Meia", 10)

carrinho.inserir_produto(p1)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p3)
carrinho.inserir_produto(p1)

carrinho.lista_produto()

print(carrinho.soma_total())
