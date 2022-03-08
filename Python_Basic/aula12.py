# Operadores Lógicos

"""
    and
    or
    not
    in - está em
    not in - não está em
"""
# x = int(input("Digite um número "))
# y = input("Qual o seu nome? ")
# if x >= 10 and x < 20:
#     print("É maior que 10 e menor que 20")
# elif x >= 20 and x < 50:
#     print("É maior ou igual à 20 e menor que 50")
# elif x >= 50:
#     print("É maior ou igual à 50")
# elif not x:
#     print("Está vazio.")
# else:
#     print("É menor que 10")
# if not y:         # Pode usar not para identificar se está vazia ou 0
#     print("Por favor coloque o valor em Y")
# if "gor" not in y:
#     print("No seu nome não possui gor")
# else:
#     print("Não exitste")


# DESAFIOOOOOOOOOOO
print("========================")
print()
print("CRIANDO SUA CONTA")
print()
print("========================")
print()
usuario = input("Crie seu usuário:.. ")
senha = input("Crie uma senha:.. ")
print()
print("========================")
if not usuario or not senha:
    print("Você não completou os requesitos")
else:
    print("Cadastro concluido com sucesso.\n Caso queira iniciar a seção digite 1: ", end="")
    y = int(input())
    if y == 1:
        print()
        secUser = input("Vamos iniciar a seção.\n Digite seu usuário: ")
        secSenha = input("Agora digite a sua senha: ")
        if usuario == secUser and senha == secSenha:
            print()
            print()
            print(f"Bem vindo à sua conta {usuario}. Aproveite e veja as novidades!")
            print("==================================")
        else:
            print("Acesso negado.\nError.\nSaindo do sistema.")
            print("=================================")
    else:
        print()
        print("Até mais.")