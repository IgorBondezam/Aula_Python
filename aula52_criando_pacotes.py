# 1° -  import aula_pacotes.modulo1                    ou
# 2° -  from aula_pacotes import modulo1               ou
from aula_pacotes.modulo1 import aumento, reducao
from aula_pacotes.formata import preco as formatamento_preco

preco = 49.90
# preco_com_aumento = aula_pacotes.modulo1.aumento(preco, 15)   - 1°
# preco_com_aumento = modulo1.aumento(preco, 15   - 2°)
preco_com_aumento = aumento(preco, 15, formatacao=True)  # 3°
print(preco_com_aumento)
preco_com_reducao = reducao(preco, 15, formatacao=True)
print(preco_com_reducao)

print(formatamento_preco.formata_real(50))


