"""
Count - itertools

start = Numero q começa a contar
step = numero de vezes q vai pular, podendo usar float numbers. Usando -1 faremos ele ir de trás para frente

"""
from itertools import count

contador = count(start=5, step=2)  # Count é um iterador, portanto posso dar next

print(next(contador))
print(next(contador))
print(next(contador))
print(next(contador))

for v in contador:
    print(v)

    if v > 20:
        break

# Uso

indice = count()
lista = ["Luiz","Maria","Jão"]
lista = zip(indice, lista)
lista = dict(lista)
print(lista[0])
