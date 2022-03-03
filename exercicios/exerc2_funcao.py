"""
Crie uma função que recebe 3 numeros como parametros e exiba a soma entre eles.
"""

def soma(x, y, z):
    if not x.isnumeric() or not y.isnumeric() or not z.isnumeric():
        return
    else:
        x = float(x)
        y = float(y)
        z = float(z)
        return x + y + z

var = soma("1","2","3")
print(var)
