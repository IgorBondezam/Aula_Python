# Função len

usuario = input("Digite seu usuário: ")
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print("Quantidade de caracteres invalida.\n Digite no mínimo 6 caracteres")
else:
    print("Você foi cadastrado!")


print(usuario, qtd_caracteres, type(qtd_caracteres))