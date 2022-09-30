"""
https://exchangeratesapi.io/
https://api.exchangeratesapi.io/latest
"""


clientes_dicionario = {
    1: {
        'nome': 'Luiz Otávio',
        'sobrenome': 'Miranda',
        'idade': 25,
        'altura': 1.80,
        'peso': 80.53,
    },
    2: {
        'nome': 'Maria',
        'sobrenome': 'Oliveira',
        'idade': 52,
        'altura': 1.67,
        'peso': 57,
    },
    3: {
        'nome': 'Pedro',
        'sobrenome': 'Faria',
        'idade': 32,
        'altura': 1.95,
        'peso': 113,
    },
}

clientes_json = """
{
    "1": {
        "nome": "Luiz Ot\u00e1vio",
        "sobrenome": "Miranda",
        "idade": 25,
        "altura": 1.8,
        "peso": 80.53
    },
    "2": {
        "nome": "Maria",
        "sobrenome": "Oliveira",
        "idade": 52,
        "altura": 1.67,
        "peso": 57
    },
    "3": {
        "nome": "Pedro",
        "sobrenome": "Faria",
        "idade": 32,
        "altura": 1.95,
        "peso": 113
    }
}
"""

import json


dado_json = json.dumps(clientes_dicionario, indent=4)
print(dado_json)

print(clientes_json)

dicionario = json.loads(clientes_json)

for chave, valor in dicionario.items():
    print(chave)
    print(valor)

with open('clientes.json', "w") as arquivo:
    json.dump(clientes_dicionario, arquivo, indent=4)

with open('clientes.json', 'r') as arquivo:
    dados = json.load(arquivo)
print()
print(dados)
print()
for chave, valor in dados.items():
    print(chave)
    print(valor)


