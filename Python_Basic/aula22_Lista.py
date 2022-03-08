# Listas em Python

"""
    Fatiamento
    append, insert, pop, del, clear, extend, +
    min, max
    range
"""
#        0  1  2     3       4     5
lista = [1, 2, 3, "string", True, 5.5]  # Acessar a lista pelos indices, assim como nas string
#       -6 -5 -4    -3     -2    -1
print(lista[5])
print(lista[-1])

lista[5] = "Add outra coisa"  # Para substituir em um indicie expecifico
print(lista[5])
print(lista[0:4:2])  # Assim como na aula 17, é possivel fazer o fatiamento, escolhendo o inicio, fim e o passo
print(lista[::-1])  # Inverter uma lista ou string de uma forma facil.

lista2 = [4, 5, 6, 7, 8, 9]

l3 = lista + lista2
print(l3)

lista.extend(lista2)  # Na lista foi extendida à lista2
print(lista)

lista2.append("B")  # Adiciona um valor no final da lista
print(lista2)

lista2.insert(0, "C")  # Adiciona um valor no indice q quiser, (indice, o que quero add)
print(lista2)

lista2.pop()
print(lista2)  # Deleta o ultimo item da lista

lista4 = []
i = 0
while len(lista4) < 10:
    lista4.append(i)
    i += 1
    print(lista4)

del (lista2[0])  # exclui um indice expecifico
del (lista4[3:8:2])

print(lista2)
print(lista4)

print(max(lista2))  # Print o maior indice da lista
print(min(lista2))  # Print o menor indice da lista

lista5 = range(0, 10)  # Faz uma contagem em um range inicial até um final, mas não sendo uma lista
print(lista5)
lista5 = list(range(0, 100, 8))  # com o comando list, ele forma uma lista com os valores
print(lista5)

# DESAFIO (jogo da forca)

print("=========================")
print()
print("Vamos jogar:")
palavra = input("Escreva uma palavra para alguém adivinhar:\n")
print()
print("=========================")
chances = 6
digitadas = []

while chances > 0:
    print(f"Você tem {chances} chances para adivinhar.")
    letra = input("Digite uma letra: ")

    if len(letra) > 1:
        print("Digite uma letra por vez.")
        continue
    digitadas.append(letra)

    if letra in palavra:
        print("Essa letra está na palavra.")
    else:
        print("Não existe essa letra na palavra. -1 chance.")
        chances -= 1
        digitadas.pop()

    palavra_temp = ''
    for letra_secreta in palavra:
        if letra_secreta in digitadas:
            palavra_temp += letra_secreta
        else:
            palavra_temp += "*"
    print(palavra_temp)

    if palavra_temp == palavra:
        print(f"Você adivinhou a palavra {palavra}. Parabéns!!")
        break

if chances == 0:
    print(f"Você perdeu, a palavra era {palavra}. ")
