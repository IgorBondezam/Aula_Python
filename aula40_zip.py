"""
Zip - Unindo iteráveis
Zip_longest - Itertools está em outro modulo
"""

from itertools import zip_longest, count

# Código

indice = count()
cidades = ["São Paulo", "Belo Horizonte", 'Salvador', "Monte Belo"]  # 4
estados = ["SP", "MG", "BA"]  # 3

cidades_estados = zip(indice, cidades, estados)  # Ele só vai unir até a menor lista
cidades_estados2 = zip_longest(cidades, estados, fillvalue="Estado")  # Ele vai unir tudo, mas o que não está associado, ira colocar none
# Fillvalue = "" faz com que substitue o none para o que você quiser
for valor in cidades_estados:
    print(valor[0], valor[1])
print("="*80)
for valor in cidades_estados2:
    print(valor[0], valor[1])

