"""
Como criar uma tupla, e seuas caracteisticas
"""

# Dá para fazer tudo igual à listas, tbm tem como criar uma tupla vazia, ou até sem parenteses

t1 = (1, 2, 3, "a", "Igor França")
t2 = 1, 2, 3, 5, 6
t3 = ()
t4 = 1,  # tbm tem como fazer uma tupla unitária, MAS PRECISA COLOCAR A VIRGULA(,)
t5 = t1 + t2

print((type(t1)))
print(type(t2))
print(type(t3))
print(type(t4))
print(t1)
# t1[1] = 8  tuplas não são editáveis, se execultar esse código ocorrerá um erro, para editar precisa
# print(t1)  transformar a tupla em uma lista
print(t1[3])
print(t5)

for v in t1:
    print(v)

print(t1[1:4])

t1 = list(t1)  # Transformar a tupla em uma lista

print(type(t1))
t1[2] = 80  # editar o valor de t1
print(t1)
t1 = tuple(t1)  # transformar t1 em uma tupla novamente
print((type(t1)))
