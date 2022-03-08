# CONDIÇÕES

"""
    If      if condição:
                O que quero execultar (vem sempre depois de 4 espaços)
    Elif
    Else    if condição:
                O que quero execultar no if
            else:
                O que quero execultar no else
"""
x = int(input("Digite um número "))

if 10 <= x < 19:
    print("É maior que 10 e menor que 19")
elif 19 <= x < 50:
    print("É maior ou igual à 19 e menor que 50")
elif x >= 50:
    print("É maior ou igual à 50")
else:
    print("É menor que 10")

