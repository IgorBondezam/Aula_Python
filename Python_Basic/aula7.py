# Formatação de string

nome = 'Igor Bondezam'
idade = 17
altura = 1.85
e_maior = idade > 18
peso = 64
IMC = peso/(altura**2)
print("O", nome, "tem", idade, "anos e seu IMC é de:", IMC, ".")
print(f"O {nome} tem {idade} anos e seu imc é de: {IMC:.4f}.")
print("O {} tem {} anos e seu imc é de: {:.4f}.".format(nome, idade, IMC))
print("O {0} tem {0} anos e seu imc é de: {1:.4f}.".format(nome, idade, IMC))
