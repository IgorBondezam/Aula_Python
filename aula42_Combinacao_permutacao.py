"""
COMBINATIONS, PERMUTATIONS e PRODUCT - Itertools
Combination - ordem não importa - Cria todas as combinações possiveis (iteravel que eu quero, número de pessoas)
permutação - ordem importa (iteravel que eu quero, número de pessoas)
ambos não repetem valores únicos
produto  - ordem importa e repete valores únicos (iteravel que eu quero, número de pessoas)
"""
from itertools import  combinations, permutations, product

pessoa = ["luiz", "André", "Eduardo", "Leticia", "Fabricio", "Rose"]

for grupo in combinations(pessoa, 2):
    print(grupo)
print("="*50)
for grupo in permutations(pessoa, 2):
    print(grupo)
print("="*50)
for grupo in product(pessoa, repeat=2):  # product precisa do repeat
    print(grupo)
