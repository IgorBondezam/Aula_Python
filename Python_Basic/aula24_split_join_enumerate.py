"""
    Split, Join, Enummerate
    * Split - Dividir uma string em lista  Transformando em lista baseado no ("que está aqui dentro")
    * Join - Transformar uma lista em str
    * Enumerate - Enumerar elementos da lista # iteráveis
"""

string = "O Brasil é o país do futebol, o Brasil é penta."

lista_1 = string.lower().split(" ")  # Estou separando os elementos em lista à cada espaço
lista_2 = string.split(",")  # Estou separando os elementos em lista à cada vírgula

print(lista_1)
print(lista_2)

for valor in lista_1:  # Estou passando em todos os elem da lista_1
    print(f"A palavra {valor} apareceu {lista_1.count(valor)}x vezes.")  # Com o count, ele conta quantas vezes a
    # palavra dentro dos parenteses apareceu

for valor in lista_2:
    print(valor.strip().capitalize())  # strip retira o espaço do começo e do fim da frase

lista_3 = ", ".join(lista_1)  # A forma que vc quer juntar, e o que vc quer juntar
print(lista_3.capitalize())

for indice, valor in enumerate(lista_1):  # enumerate do que vc quer, sendo que a primeira variavel do for, será
    print(indice, valor, len(lista_1))  # usado para colocar o valor do enumerate

lista = [
    [1, 2],
    [3, 4],
    [5, 6]
]
print(lista)

for indice, valor in enumerate(lista):
    print(indice, valor)


