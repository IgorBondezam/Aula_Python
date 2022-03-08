"""
Criando meus próprios módulos
"""

import math

PI = math.pi


def dobra_lista(list):
    return [x * 2 for x in list]


def multiplica(list):
    r = 1
    for i in list:
        r *= i
    return r

if __name__ == "__main__":  # Para n ser execultado aonde ele for importado
    lista = [1,2,3,4,5]
    print(dobra_lista(lista))
    print(multiplica(lista))

    print(__name__)
print(PI)  # O PI será execultado em qualquer lugar q for importado



