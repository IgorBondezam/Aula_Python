"""
    While / Else
"""

contador = 0
acumulador = 0


while contador <= 10:
    print(contador, acumulador)
    acumulador = acumulador + contador
    if acumulador > 30:
        break
    contador += 1  # O else será execultado quando o while acabar, mas se houver um break, o else n é execultado
else:
    print("O while acabou aqui")
    contador = 5  # Mesmo com o contador alterando, uma vez q saiu do while, n volta.
