from random import randint
import CNPJ_funçoes


def complementos(codigo):
    resultado = CNPJ_funçoes.multiplica(codigo)
    return str(CNPJ_funçoes.equacao(resultado))


cnpj = str(randint(10000000, 99999999))
cnpj = cnpj + "0001"
x = complementos(cnpj)
y = complementos(cnpj + x)
print(cnpj)
print()
print("="*50)
print()
print(f"O CNPJ gerado foi {CNPJ_funçoes.formatar(cnpj) + x + y}")
print()
print()
print("="*50)
