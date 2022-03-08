"""
    For / Else em Python
"""

variavel = ["Luiz Otávio", "Joãozinho", "Maria"]
comeca_c_j = 0
for valor in variavel:
    if valor.lower().startswith("j"):    # startswith: função para achar uma string que começa com(letra que queira)
        print(valor)
        comeca_c_j += 1
else:  # Esse else, só será execultado se o for INTEIRO for percorrido
    print(f"há {comeca_c_j} palavras que começa com J.")

for valor2 in variavel:
    if valor2.lower().startswith("m"):
        print(valor2)
        break  # Como há esse BREAK, o else não será execultado
else:
    print("Eu gosto de M.")
