"""
Fizz Buzz - se o parametro da funcao for divisivel por 3, retorne fizz, se o parametro for divisivel por 5,
retorne buzz, se for divisivel por 3 e por 5, retorne FizzBuzz, caso contrario retorne o numero enviado
"""


def divisivel(x):
    if x%5 == 0 and x%3==0:
        return "FizzBuzz"
    elif x%5 == 0:
        return "Buzz"
    elif x%3 == 0:
        return "Fizz"
    else:
        return x


from random import  randint

for i in range(100):
    aleatorio = randint(0,100)
    print(divisivel(aleatorio))
    