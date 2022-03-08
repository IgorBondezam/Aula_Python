"""
Scopo de variaveis em funcoes e globais
"""

variavel = "Valor"


def func():
    print(variavel)


def func2():
    variavel = "Calor"
    print(variavel)


def func3(arg):
    arg = arg.replace('V', 'C')
    return arg


def func4():
    global variavel
    variavel = 'Calor'



func()
func2()
outra_variavel = func3(variavel)
print(variavel)
print(outra_variavel)
func4()
print(variavel)


