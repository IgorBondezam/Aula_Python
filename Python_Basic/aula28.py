"""
Expressões condicionais com OR
"""

nome = input("Qual o seu nome? ")

if nome:
    print(nome)
else:
    print("Você não digitou nada =(")

print(nome or "Você não digitou nada!")  # Se nome tiver algo, diferente de 0, uma lista vazia, algo vazio
# false, coisas vazia no geral, ele escreve o nome, caso não, escreve a outra msg
# Resumindo, se for vdd ele exibe, se n não exibe ( Para na primeira vdd que achar)

a = None  # Falso
b = False  # Falso
c = 0  # Falso
d = []  # Falso
f = 22  # Verdadeiro  PARA AQUI, 1° VERDADEIRA
g = 'Igor'  # Verdadeiro
variavel = a or b or c or d or f or g

print(variavel)
