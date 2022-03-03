"""
    Faça um programa que peça ao usuário para digitar um número inteiro, informe
    se este número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é um.
"""

n_user = input("Digite um número inteiro: ")
print()

try:
    n_user = int(n_user)

    if n_user % 2 == 0:
        print("Seu número é par.")
    else:
        print("Seu número é ímpar.")

except:
    try:
        n_user = float(n_user)
        print("Você digitou um número real, não inteiro.")
    except:
        print("Você não digitou um número.")
