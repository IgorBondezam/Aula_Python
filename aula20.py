"""
    Iterando strings no while
"""

# Índices
#        0123456789...................... 33
frase = "o rato roeu a roupa do rei de roma"
taman_frase = len(frase)
nova_frase = ""

i = 0


select_letra = input("Qual letra você gostaria que ficasse maiúscula? ")

while i < taman_frase:
    letra = frase[i]
    if letra == select_letra:
        nova_frase += select_letra.upper()
    else:
        nova_frase += letra
    i += 1
print(nova_frase)