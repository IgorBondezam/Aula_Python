"""
04.252.011/0001-10 40.688.134/0001-61 71.506.168/0001-11 12.544.992/0001-05

0   4   2   5   2   0   1   1   0   0   0   1
5   4   3   2   9   8   7   6   5   4   3   2
0   16  6   10  18  0   7   6   0   0   0   2 = 65
Fórmula -> 11 - (65 % 11) = 1
Primeiro digito = 1 (Se o digito for maior que 9, ele se torna 0)

0   4   2   5   2   0   1   1   0   0   0   1   1   X
6   5   4   3   2   9   8   7   6   5   4   3   2
0   20  8   15  4   0   8   7   0   0   0   3   2 = 67
Fórmula -> 11 - (67 % 11) = 10 (Como o resultado é maior que 9, então é 0)
Segundo digito = 0

Novo CNPJ + Digitos = 04.252.011/0001-10
CNPJ Original =       04.252.011/0001-10
Válido

Recap.
543298765432 -> Primeiro digito
6543298765432 -> Segunro digito
"""
import CNPJ_funçoes

while True:
    print("=" * 50)
    print()
    cnpj_nome = input("Insira o CNPJ para ser validado:")
    print()
    print("=" * 50)

    if len(cnpj_nome) > 18:
        print("CNPJ INVÁLIDO. NÚMERO DE CARACTERES ALÉM DO LIMITE")
        continue
    cnpj_sem_fim = CNPJ_funçoes.tira_dois(cnpj_nome)
    if not cnpj_sem_fim:
        print("O SEU CNPJ É UMA SEQUENCIA, PORTANTO NÃO É VÁLIDO.")
        continue

    cnpj_num = CNPJ_funçoes.tira_caracter(cnpj_sem_fim)

    mult1 = CNPJ_funçoes.multiplica(cnpj_num)
    if not mult1:
        print("Você digitou uma letra.")
        continue

    resultado01 = CNPJ_funçoes.equacao(mult1)
    if resultado01 > 9:
        resultado01 = 0

    mult2 = CNPJ_funçoes.multiplica(cnpj_num + str(resultado01))

    resultado02 = CNPJ_funçoes.equacao(mult2)
    if resultado02 > 9:
        resultado02 = 0

    if cnpj_num + str(resultado01) + str(resultado02) == CNPJ_funçoes.tira_caracter(cnpj_nome):
        print(f"VERIFICAÇÃO FEITA COM SUCESSO, O CNPJ {cnpj_nome} É VALIDO.")
    else:
        print(f"O CNPJ {cnpj_nome} NÃO É VALIDO. ELE DEVERIA SER {CNPJ_funçoes.formatar(cnpj_num) + str(resultado01) + str(resultado02)}. ")
