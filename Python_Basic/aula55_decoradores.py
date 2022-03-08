def fala_oi():
    print("Oi")


def master(funcao):
    def slave():
        print("Agora estou decorada.")
        funcao()
    return slave


fala_oi()  # Já essa função variavel é a FUNCAO FUNCAO fala_oi
fala_oi = master(fala_oi)  # Para não fazer isso, podemos fazer assim     ↓
    #    ↑                                                                ↓
fala_oi()  # Essa função fala_oi, está decorada como a master(fala_oi)    ↓
#                                                                         ↓


def main(funcao):
    def slave():
        print("Agora estou decorada.")
        funcao()
    return slave


@main  # essa função foi decorada na main
def fala_tchau():
    print("Tchau")

fala_tchau()

from time import time
from time import sleep


def velocidade(funcao):
    def interna(*args, **kwargs):
        start_time = time()
        resultado = funcao(*args, **kwargs)
        end_time = time()
        tempo = (end_time - start_time) * 1000
        print(f"A função {funcao.__name__} levo {tempo:.2f}ms para executar.")
        return resultado
    return interna


@velocidade
def demora():
    for i in range(5):
        sleep(1)

demora()





