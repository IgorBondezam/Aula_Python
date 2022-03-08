"""
Funções - def em Python
          return
"""


def funcao():  # para determinar uma função se usa, def nome_da_função (parâmetro):
    print("Hello World!")                           #   O que será desenvolvido


def mensagem(msg="tudo bem", nome="Usuário"):
    print(msg.replace("e", "3"), nome.replace("r", "s2").replace("R", "S2"))  # Replace, substitui o que vc quer da str por outra coisa


def funcao_invalida(men):
    print(men)


def funcao_valida(men):
    return men
    print("Isso não será executado")


funcao()
mensagem()
mensagem("SIMMM")
mensagem("SIMMM", "João")
mensagem(nome="Mário", msg="Tudo legal")
mensagem(nome="Rodrigo")
print(mensagem)

variavel = funcao_invalida("Valor que eu quero")
print(variavel)  # Nesse caso, como a função não possui return, ela n volta nenhum valor, dando como resultado None

variavel = funcao_valida("")
print(variavel)  # Como nessa função há o return, ela ira retornar o valor do men, associando o valor à variavel

