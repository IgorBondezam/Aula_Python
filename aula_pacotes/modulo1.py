from aula_basica_python.aula_pacotes.formata import preco

def aumento(valor, porcentagem, formatacao = False):
    r = valor + (valor * porcentagem / 100)
    if formatacao:
        return preco.formata_real(r)
    else:
        return r


def reducao(valor, porcentagem, formatacao = False):
    r = valor - (valor * porcentagem / 100)
    if formatacao:
        return preco.formata_real(r)
    else:
        return r
