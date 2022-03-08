"""
    Desempacotamento de lista
"""
lista = ["luiz", "João", "Maria",1,2,3,4,5,6,7,8,9]

n1, n2, *outra_lista, antepenultimo, ultimo_da_lista = lista  # Para desempacotar uma lista, é necessário criar
# variaveis de acordo
# com a quantidade
# de itens na lista.
# n3, n4 = lista Como por exemplo, na lista há 12 itens, e aqui há 2 variaveis, portanto
# print(n3) não irá ocorrer
print(n2)  # Mas como coloquei * ali, ele gerará uma outra lista
print(outra_lista)
print(antepenultimo)
print(ultimo_da_lista)
