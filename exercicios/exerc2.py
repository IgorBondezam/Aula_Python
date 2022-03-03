"""
    Faça um programa que pergunta a hora ao usuário e, baseando-se no horário descrito, exiba a saudação
    apropriada
"""

nome = input("Olá, qual o seu nome? ")
horario = input(f"Olá {nome} que horas são agora?\n ")
print()

try:
    horario = float(horario)

    if  6 <= horario < 12:
        print(f"Bom dia {nome}.")

    elif 12 <= horario <= 18:
        print(f"Boa tarde {nome}.")
    elif 0 < horario > 24:
        print("O horário deve estar entre 0 e 24.")
    else:
        print(f"Boa noite {nome}.")
except:
    print("Você não digitou um número.")