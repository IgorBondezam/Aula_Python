from random import randint

cpf_cliente = str(randint(100000000, 999999999))

soma = 0
soma_01 = 0

for digito, cont in enumerate(range(10, 1, -1)):
    soma = int(cpf_cliente[digito]) * cont
    soma_01 += soma

digito_01 = 11 - (soma_01 % 11)

if digito_01 > 9:
    digito_01 = 0

soma = 0
soma_01 = 0
ult_soma = 0

for digito, cont in enumerate(range(11, 2, -1)):
    soma = int(cpf_cliente[digito]) * cont
    soma_01 += soma
    ult_soma = digito_01 * 2

digito_02 = 11 - ((soma_01 + ult_soma) % 11)

if digito_02 > 9:
    digito_02 = 0

cpf_confirm = ""

for digito, cont in enumerate(range(11, 2, -1)):
    cpf_confirm += cpf_cliente[digito]

sequencia = cpf_confirm + str(digito_01) + str(digito_02) == str(cpf_confirm[0] * len(cpf_cliente))
cpf_confirm = cpf_confirm + str(digito_01) + str(digito_02)

print("=" * 20)
print()
print(f"Geramos o CPF {cpf_confirm}. Use com responsabilidade.")
print()
print("=" * 20)
