"""
Groupby - Itertools
"""
from itertools import groupby, tee

alunos = [
    {"nome": "Luiz", "nota": "B"},
    {"nome": "Leticia", "nota": "A"},
    {"nome": "Joana", "nota": "C"},
    {"nome": "João", "nota": "A"},
]
alunos.sort(key=lambda item: item["nota"])
print(alunos)
alunos_agrupados = groupby(alunos, lambda item: item["nota"])


for agrupado, valores in alunos_agrupados:
    va1, va2 = tee(valores)
    print(agrupado)
    quantidade = len(list(va1))

    for nome in va2:
        print(f"{nome['nome']} tirou {nome['nota']}")

    print(f"{quantidade} alunos tiraram {agrupado}")
