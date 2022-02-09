"""
    For in em Python

    Função range(start = 0, stop, step=1)
"""
texto = "Olá mundo. tudo bom"
novo_texto = ""

for letra in texto:
    if "." in letra:
        novo_texto += letra
        novo_texto += "\n"
    else:
        novo_texto += letra
print(novo_texto)
# for n in range(5, 10, 1):  # Por padrao, dentro do range o inicio vem com 0 e o step vem com 1
#     print(n)  # Por tanto eu posso emitir o inicio e o step
#
# for x in range(10):  # Aqui ele vai de 0 até 10 mas nunca aparece o stop.
#     print(x)

