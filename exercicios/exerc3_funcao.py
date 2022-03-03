"""
Crie uma funcao que receba 2 numeros. o primeiro é um valor e o segundo um percentual. Retorne o valor do primeiro
mais o aumento do percentoal do msm
"""


def porcento (x, y):
    return (x * y/100) + x


a = input("Digite um número: ")
b = input("Digite a porcentagem que deseja aumenta-lo: ")

if not a.isnumeric() or not b.isnumeric():
    print("Digite apenas números.")
else:
    a = float(a)
    b = float(b)
    porcent = porcento(a, b)
    print(porcent)
