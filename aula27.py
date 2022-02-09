"""
    Operador ternário em Python
"""

# logged_user = False
# logado = input("Digite 1 para logar.")
#
# if logado == "1":
#     logged_user = True
#
# if logged_user:
#     msg = "Usuário logado."
# else:
#     msg = "Usuário precisa logar."
# print(msg)

logged_user = False
msg = "Usuário logado." if logged_user else "Usuário precisa logar."
# Mensagem do if
                        # If e a condição
                                        # Else e a mensagem que irá mostrar(no else)
print(msg)  # Nesse caso fizemos o if else na frente da mensagem verdadeira (do if)
