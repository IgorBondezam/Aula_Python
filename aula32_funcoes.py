"""
função lambda
"""

# def funcao (arg, arg2):    ao invez de criar uma função assim
#    return arg * arg2          se pode usar lambda
#
# var = funcao(2,2)

a = lambda x, y: x * y  # Essa é a mesma coisa que aquela função, sendo o que está depois do : é o que acontecerá no return

print(a(2, 2))


def func(item):
    return item[1]  # criando essa função para servir de paramentro no sort key, atráves do primeiro parametro das listas


lista = [
    ["P1", 13],
    ["P2", 20],
    ["P3", 14],
    ["P4", 69],
    ["P5", 30],
    ["P6", 60]
]

lista.sort()  # A função sort ela muda a ordem das listas, mas no caso ele não há nenhum parametro q está sendo medido

print(lista)

lista.sort(key=func)

print(lista)

lista.sort(key=lambda item: item[1], reverse=True)  # Mas para não ter que criar uma função só pra isso, usamos lambda
# e o reverse serve para fazer de trás pra frente

print(lista)

print((sorted(lista, key=lambda i: i[1])))  # Uma forma  mais enxuta para fazer

