"""
CPF = 168.995.350-09
------------------------------------------------
1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
8 * 8  = 64           #    8 *  9 = 72
9 * 7  = 63           #    9 *  8 = 72
9 * 6  = 54           #    9 *  7 = 63
5 * 5  = 25           #    5 *  6 = 30
3 * 4  = 12           #    3 *  5 = 15
5 * 3  = 15           #    5 *  4 = 20
0 * 2  = 0            #    0 *  3 = 0
                      # -> 0 *  2 = 0
         297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

while True:
    print("=" * 20)
    print()
    cpf_cliente = input("Digite seu CPF para ser validado: ")
    print()
    print("=" * 20)

    if not cpf_cliente.isdigit():
        print()
        print("Você precisa digitar o NÚMERO do seu CPF.")
        print()
    elif len(cpf_cliente) < 9 or len(cpf_cliente) > 11:
        print()
        print("Você não digitou a quantidade de caracteres válidos para validar o cpf.")
        print()
    else:
        soma = 0
        soma_01 = 0

        for digito, cont in enumerate(range(10, 1, -1)):
            soma = int(cpf_cliente[digito]) * cont
            soma_01 += soma

        digito_01 = 11 - (soma_01 % 11)
        print(digito_01)

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

        print("=" * 20)
        print()
        if cpf_confirm + str(digito_01) + str(digito_02) == cpf_cliente and not sequencia:
            print(f"CPF {cpf_confirm + str(digito_01) + str(digito_02)} válido.")
        else:
            print(
                f"CPF {cpf_cliente} inválido.\nO resultado correto seria {cpf_confirm + str(digito_01) + str(digito_02)}.")
        print()
        print("=" * 20)
