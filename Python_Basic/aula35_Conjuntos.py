""" Conjuntos | Sets
ELES NÃO RESPEITAM ORDENS, CADA HORA ESTÁ EM UM LUGAR DIFERENTE
NÃO ACEITA ELEMENTOS DUPLICADOS
SETS ITERAM AS COISAS POSTAS NELE
add (adiciona), ipdate (atualiza), clear, discard
union | (une)
intersection & (todos os elementos presentes nos dois sets)
dofferemce - (elementos apenas no set da esquerda)
symmetric_difference ^ (Elementos que estão em dois sets, mas não em ambos)
"""

s1 = set()  # Para fazer um set vazio, precisa fazer dessa forma, pois s1= {} é um dicionário
s1.add(1)  # para adicionar valores ao set
s1.add(2)
s1.add(3)
s1.add(3)  # Add dois 3, mas será mostrado só 1, pois não aceita elementos duplicados
s1.add((1,2,3,"Ola mundo"))  # adicionar uma tupla

s1.discard(2)

s1.update("python")

for v in s1:
    print(v)

l1 = [1,1,1,1,2,3,4,5,6,7,1,1,1,]  # Lista
print(l1)
l1 = set(l1)  # set  aqui não sairá varios 1, pois set não aceita elementos duplicados
print(l1)

s1 = {1,2,3,4,5,7}
s2 = {1,2,3,4,5,6}
s3 = s1 | s2  # union é simbolizado pelo |
print(s3)
s3 = s1 & s2  # intersection é simbolizado pelo & (mesma coisa que intersessão na matemática)
print(s3)
s3 = s2 - s1  # difference é simbolizado pelo - (mesma coisa que diferenca de conjuntos na matemática)
print(s3)
s3 = s1 ^ s2  # symmetric_diference é simbolizado pelo ^ (Irá mostrar o que tem de diferente nos dois)
print(s3)