# Sequences = lists, tuples, str - iteravel

nome = "Igor França"

for letra in nome:  # for converta o nome para iterador, e colocar o valor de next em letra
    print(letra)

print("-"*80)

iterador = iter(nome)

try:
    print(next(iterador))  # i
    print(next(iterador))  # g
    print(next(iterador))  # o
    print(next(iterador))  # r
    print(next(iterador))  #
    print(next(iterador))  # f
    print(next(iterador))  # r
    print(next(iterador))  # a
    print(next(iterador))  # n
    print(next(iterador))  # ç
except:
    pass

print("Cade os valores?")
for v in iterador:
    print(v)






