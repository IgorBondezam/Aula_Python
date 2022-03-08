"""
MANIPULAÇÃO DE STRINGS

STRING INDICES
FATIAMENTO DE STRING [inicio:fim:passo]
FUNÇÕES BUILT-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

https://docs.python.org/3/library/functions.html (função built-in)
https://docs.python.org/3/library/stdtypes.html (tipos built-in)
"""

# ===============================================

# Posivitos
#       [012345678]
texto = "Python_s2"
#      -[987654321]0[123...]
# Negativos

# ===============================================

print(texto[-1])  # acessar um unico indice negativo
print(texto[0])  # acessar um unico indice positivo
print(texto[:5])  # acessar até aquele indice (inicio:fim -> 0:5 ou :5) mas ele n é incluido
print(texto[:-1])  # acessar até aquele indice (inicio:fim -> 0:-1 ou :-1)

print(texto[1:6])  # inicio:fim da string

print(texto[::3])  # Pular caracter ( inicio:fim:passo -> 0:0:3 ou ::3) -> Inicio fim pulando de 3 em 3
print(texto[1:6:2])  # Pular caracter ( inicio:fim:passo -> 0:0:3 ou ::3) -> Inicio(1) fim(6) pulando de 2 em 2

print(len(texto))  # número de indices da sting pulando o 0
