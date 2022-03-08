from dados_para_aula44_fim import  produtos, pessoas, lista
from functools import reduce

acumula = 0
for item in lista:
    acumula += item

print(acumula)
soma_lista = reduce(lambda ac, i: i + ac, lista, 0)  # acumulador, item da lista: item da lista + acumulador, lista, inicio do acumulador
print(soma_lista)

soma_precos = reduce(lambda ac, p: p["preco"] + ac, produtos, 0)
print(soma_precos / len(produtos))
