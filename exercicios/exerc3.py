"""
    Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva
    "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva
    "Seu nome é muito grande".
"""

nome = input("Olá, qual o seu nome? ")

numero_letras = len(nome)

if numero_letras <= 4:
    print(f"Seu nome, {nome}, é muito curto.")
elif numero_letras == 5 or numero_letras == 6:
    print(f"Seu nome, {nome}, é normal.")
else:
    print(f"Seu nome, {nome}, é muito grande. ")