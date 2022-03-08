"""
Dicionários - uma lista na qual você controla o indice, key.
dicionario = {nome da chave : item que queira}
"""

d1 = {"chave1": "valor da chave"}

print(type(d1))
print(d1)

d1[
    'nova_chave'] = 'Valor da nova chave'  # Adicionei mais um elemento ao dicionario, com nova_chave como chave desse valor
print(d1)
print(d1["nova_chave"])

d2 = dict(chave1="Valor da chave", chave2="Valor da outra chave")  # Outra forma de criar um dicionario
print(d2)
print(d2['chave2'])

d3 = {"chave": "valor1", "chave": "valor2", "chave": "valor3", "chave": "olá mundo"}
print(d3)  # nesse caso, como as chaves são as mesmas, ela vai atribuir o valor da ultima coisa que foi atribuida

d4 = {  # São usados como chave, geralmente valores imutaveis
    'str': "String como chave",
    123: "Inteiros como chave",
    (1,2,3,4): "Tupla como chave",
}

print(d4[(1,2,3,4)])
d4[(1,2,3,4)] = "Novo valor da tupla"  # modificando valor do dicionario
print(d4)
if 'nãoexiste' in d4:  # Analizando se existe a chave especifica no dicionario, obs: não coloque a chave entre colchetes
    print(d4['nãoexiste'])  # Se eu der print em uma chave que não existe, ele dará erro
print("Depois do if")

del d4["str"]  # deletando valor do dicionario
print(d4)

if "Inteiros como chave" in d4.values():  # identificar se há um valor no dicionario
    print(len(d4))

for k in d4:
    print(k)
for i in d4.values():
    print(i)
for b in d4.items():
    print(b)
for c, v in d4.items():
    print(c, v)

clientes = {  # dicionario dentro de outro dicionario
    "cliente1": {
        "nome" : "igor",
        "sobrenome" : "Bondezam",
    },
    "cliente2": {
        "nome" : "joao",
        "sobrenome" : "Almeida",
    },
}

for clientes_k, clientes_v in clientes.items():  # clientes_k entra em clientes e pega o primeiro item(clientes)(a chave)
    print(f"Exibindo {clientes_k}")  # clientes_v pega o segundo que é o segundo dicionario
    for dados_k, dados_v in clientes_v.items():  # dentro do segundo dicionario, dados_k pega a chave e dado_v pega o valor
        print(f"\t {dados_k} = {dados_v}")  # \t para dar um espaço de paragrafo(Como o tab)

