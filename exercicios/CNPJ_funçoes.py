def tira_caracter(cnpj):
    try:
        cnpj = cnpj.replace("/", "")
        cnpj = cnpj.replace(".", "")
        cnpj = cnpj.replace("-", "")
        cnpj = cnpj.replace(" ", "")
        return cnpj
    except:
        pass


def tira_dois(cnpj):
    if sequencial(cnpj):
        return False
    else:
        if len(cnpj) == 18:
            cnpj = cnpj[:16]
            return cnpj
        elif len(cnpj) == 17:
            cnpj = cnpj[:16]
            return cnpj
        elif len(cnpj) > 12 or len(cnpj) < 15:
            cnpj = cnpj[:-2]
            return cnpj
        else:
            return cnpj


def multiplica(cnpj):
    mult = 0
    try:
        if len(cnpj) > 12:
            x = 6
            for i in cnpj:
                mult += int(i) * x
                x -= 1
                if x == 1:
                    x = 9
            return mult

        else:
            x = 5
            for i in cnpj:
                mult += int(i) * x
                x -= 1
                if x == 1:
                    x = 9
            return mult
    except:
        return False


def equacao(result):
    formula = 11 - (result % 11)
    return formula


def sequencial(cnpj):
    if tira_caracter(cnpj) == cnpj[0] * len(tira_caracter(cnpj)):
        return True
    else:
        return False
