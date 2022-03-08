"""
 Funçoes - *args **kwargs -
"""


# def func (a1, a2, a3, a4, a5, nome = None, a6):  # A partir do momento q usei =, todos depois dele precisa ser definido tbm
#     print(a1, a2, a3, a4, a5, nome, a6)
#
# func(1,2,3,4,5, nome = "Luiz", a6 = 5)  # mesma coisa acontece aqui, depois que um foz definido pelo nome os depois


def func2(*args, **kwargs):  # Se eu n sei a quantidade de argumento q será necessário para a função, uso *args para n limitar ela
    print(args)
    print(kwargs)
    nome = kwargs["nome"]
    print(nome)
    idade = kwargs.get('idade')  # metodo get analisa se existe, se existe pega o valor, caso n, deixa em branco
    print(idade)
    sobrenome = kwargs.get("sobrenome")
    print(sobrenome)  # nesse caso ele printa none, mas não ocorre um erro como aconteceria em
    # sobrenome = kwargs['sobrenome']

func2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 22, nome = "igor", idade = 18)  # args não possui palavras chaves, já kwargs são
# o que apresentam palavras chaves como nome ou idade
