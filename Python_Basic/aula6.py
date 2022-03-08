# VARIÁVEIS

nome = 'Igor Bondezam'
idade = 17
altura = 1.85
e_maior = idade > 18
peso = 64

print("Nome:..", nome, "Idade:..", idade, "Altura:..", altura, "É maior de idade:..", e_maior, sep='\n')
print("\n")
print(idade * (nome + "      "))
print("\n")
IMC = peso/(altura**2)
print("O", nome, "tem", idade, "anos e seu IMC é de:", IMC, ".")
