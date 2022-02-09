# ENTRADA DE DADOS

nome = input("Qual o seu nome ? ")
idade = int(input("Qual a sua idade ? "))  # Para fazer o input outro valor dif de str coloque o tipo dele primeiro
ano = 2022
print()
print(f"Olá {nome}. O tipo da variável é {type(nome)}")
print(f"Sua idade é: {idade}")
print(f"Você nasceu em {ano - idade}")


