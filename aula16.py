"""
    Formatação de strings
    :s - Texto (strings)
    :d - inteiros (int)
    :f - Números de ponto flutuante (float)
    :.(NÚMERO)f - Quantidade de casas decimais (float)
    :(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

    > - Esquerda
    <- Direita
    ^ - Centro
    .upper() - MAIUSCULA
    .lower() - minusculo
    .title() - Primeiras Letras Maiusculas
"""

num_1 = 16
num_2 = 3
divisao = num_1 / num_2
print("{:.2f}".format(divisao))
print(f"{divisao:.2f}")

print(f"{num_1:0>10}")
print(f"{num_1:0<10}")
print(f"{num_1:0^10}")
print(f"{num_1:0>10.2f}")

nome = "Grande mago"
print(f"{nome:#^51}")

nome_format = '{:@>50}'.format(nome)
print(nome_format)
