# TIPO DE DADOS

"""
    str - string - textos 'Assim' ou "Assim"
    int - inteiro - 123456 ou 0 ou -123456 ... (sem ponto )
    float - real/ponto flutuante 123.5 ou 142.9 ou -1477.8 ou 0.0 (se tiver ponto irá ser float)
    bool - booleano/lógico - True ou False 10==10 (retornará True) 10==20 (retornará False)
"""
print(type("Olá Mundo"))
print(type(1477))
print(type(0.0))
print(type(True))
print(type(False))
print('\n')
print(type("Luiz"), type(123), type(True), type(0.0), sep='\n')
print("\n")
print(type(10 == 10), type("l" == "s"))
print((10 == 10))
print("l" == "s")
print("\n")

# MUDANÇA DE TIPO
print("----------------------------")
print("luiz", type("Luiz"), bool('luiz'))
print(0, type(0), bool(0))  # bool com 0 ou '' ou [] {} (coisas vazia) ele dá false
print(10.0, type(10.0), str(10.0), type(str(10.0)), int(10.5), type(int(10.5)), "10.5", float("10.5"), float(5), sep='  ')
print("\n")

#DESAFIO
print("================================")
print("Igor Bondezam França", type("Igor Bondezam França"), sep="--")
print(17, type(17), sep="--")
print(1.85, type(1.85), sep="--")
print(17>18, type(17>18), sep="--")
