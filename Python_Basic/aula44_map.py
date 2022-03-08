from dados_para_aula44_fim import produtos, pessoas, lista


def aumenta_preco(p):
    p["preco"] = round(p["preco"] * 1.05, 2)
    return p


nova_lista = map(lambda x: x * 2, lista)
print(list(nova_lista))

nova_lista = [x * 2 for x in lista]
print(nova_lista)

precos = map(aumenta_preco, produtos)

for preco in precos:
    print(preco)
