"""
Crie uma funcao que receba ma funcao2 como parametro e retorne o valor da funcao2 execultada
Faça a funcao executar duas funcoes que recebam um numero diferente de argumetos
"""


def ola_nome(nome):
    return f"Olá {nome}!"


def ola(nome, saudacao):
    return f"{saudacao} {nome}"


def funcao1(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)


executando = funcao1(ola_nome, "Lucio")
executando2 = funcao1(ola, "lucio", saudacao="Bom dia!")
print(executando)
print(executando2)
