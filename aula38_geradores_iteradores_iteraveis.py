"""
Iteravel = é aquele q pode iterar sobre ele, mas não necessariamente é um iterador
iterador = vai te dar um valor de cada vez, sempre q precisar desse valor
geradores = são usados, quando algo vai oculpar muito espaço na memoria ou demorará para ser processado, ele gera um valor
quando for usar esse valor
"""

import sys
import time


def gera():
    r = []
    for n in range(100):
        r.append(n)  # Coloca no array
        time.sleep(0.1)  # tempo de delay de 0.1 seg
    return r


def funcao_geradora():
    for n in range(100):
        yield n  # faz com que ele passe para a variavel que receber o valor, o valor a cada momento.
        # não tudo de uma vez, mas sim de tempo em tempo
        time.sleep(0.1)


lista = [0,1,2,3,4,5]

print(hasattr(lista, "__iter__"))  # Para ver se a lista é um iteravel

lista = 12345
print(hasattr(lista, "__iter__"))

lista = list(range(10))
print(sys.getsizeof(lista))  # Saber quanto de memoria em bits, q, nesse caso a lista, está ocupando

g = gera()

for v in g:  # Estamos simulando algo pesado para ser carregado
    print(v)  # Ele demora para aparecer por causa do time.sleep

print("="*50)
g = funcao_geradora()

print(g)  # objeto gerador, e aonde está alocado na memória

print(hasattr(g, "__iter__"))  # iteravel
print(hasattr(g, "__next__"))  # iterador

print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

print("="*60)

for v in g:
    print(v)  # Quando ele cria o valor, ele ja lança, não espera todos ficar prontos e lançar todos

print(sys.getsizeof(g))

# """
# forma pra criar um gerador
# """

l1 = [x for x in range(100)]  # lista compreenção
print(type(l1))
print(sys.getsizeof(l1))
l2 = (x for x in range(100))  # gerador
print(type(l2))
print(sys.getsizeof(l2))


