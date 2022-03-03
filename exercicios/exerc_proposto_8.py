"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
Some os valores nas listas retornando uma nova lista com os valores somados:
Se uma lista for maior que a outra, a soma só vai considerar o tamanho da
menor.
Exemplo:
lista_a     = [1, 2, 3, 4, 5, 6, 7]
lista_b     = [1, 2, 3, 4]
=================== resultado
lista_soma  = [2, 4, 6, 8]
"""

l1 = [1,2,3,4,5,6,7,8,9]
l2 = [3,4,5,6,7,8]

soma = []
l3 = zip(l1, l2)
for v in l3:
    soma += [v[0] + v[1]]
print(soma)
