carrinho = []

carrinho.append(("Produto 1", 30))
carrinho.append(("Produto 2", 20))
carrinho.append(("Produto 3", 0))
carrinho.append(("Produto 4", 50))


total = [v[1] for v in carrinho]

print(sum(total))
