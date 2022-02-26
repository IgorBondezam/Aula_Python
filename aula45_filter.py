from dados_para_aula44_fim import produtos, pessoas, lista

nova_lista = filter(lambda x: x>5, lista)
print(list(nova_lista))

filtro_preco = filter(lambda p: p["preco"] < 10, produtos)
for produto in filtro_preco:
    print(produto)
