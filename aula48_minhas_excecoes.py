"""
Criando minhas proprias excecoes
"""


def divide(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError as error:
        print("Log: ", error)
        raise


def dividir(n1, n2):
    if n2 == 0:
        raise ValueError('n2 não pode ser 0.')
    return n1/n2


try:
    print(divide(2, 0))
except ZeroDivisionError as error:
    print(error)

try:
    print(dividir(2,0))
except ValueError as error:
    print(error)

