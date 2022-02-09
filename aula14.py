# https://docs.python.org/3/library/stdtypes.html  (documentação python)

num1 = input("Digite um número: ")
num2 = input("Digite outro número: ")

# isnumeric, isdigit e isdecimal faz com que avaleie e volta um bool se a string pode ser transformado em int
# Mas essas funções só mostraram os números positivos sem .

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else:
    print("Não pude transformar sua informação para número")

# try e except funciona assim: ele irá tentar execultar, se algo de errado acontecer vai para o except


try:
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
except:
    print("Não pude transformar sua informação para número")