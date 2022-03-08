# https://docs.python.org/3/library/functions.html#open
# Aula 89
#                       ↓
file = open("abc.txt", "w+")  # Cria um arquivo txt, w+ permite a gente ler e escrever nele
# with open("acb.txt", "w+") as file:    - UMA FORMA DE ABRIR O ARQUIVO SEM TER Q FECHAR
file.write("Linha 1\n")  # add coisas nele
file.write("Linha 2\n")  # add coisas nele
file.write("Linha 3\n")  # add coisas nele

file.seek(0, 0)  # Para ele fazer a leitura do começo do arquivo
print("Lendo Linhas: ")
print(file.read())
print("##########")

file.seek(0, 0)
print(file.readline())  # ler linha por linha
print(file.readline())
print("##########")

file.seek(0, 0)
print(file.readlines())  # Joga linha por linha em uma lista
print("##########")

file.seek(0,0)
for x in file.readlines():
    print(x)
print("##########")


file.close()  # fecha o arquivo

# PARA DELETAR
import os

os.remove("abc.txt")

print("ARQUIVO JSON\n")

import json
d1 = {
    "Pessoa 1": {
        "nome": "Luiz",
        "idade": 25,
    },
    "Pessoa 2": {
            "nome": "Marta",
            "idade": 30,
        },
}

d1_json = json.dumps(d1, indent=True)
print(d1_json)



