# Laços de repetição WHILE
"""
while condicao:
    o que ocorrerá
"""
i = 0
while i < 10:
    print("#" * i)
    i = i + 1
i = 10
while i > 0:
    print("#" * i)
    i = i - 1

while i < 10:
    if i == 5 or i == 8:
        i += 1  # x = x + 1
        continue   # O continue pula uma repetição, sempre q ver continue ele pula para o outro

    print(i)
    i = i + 1

while i > 0:
    if i == 2:
        print("Acabou esse laço")
        break  # Sai do laço, ACABA A REPETIÇÃO
    print(i)
    i = i - 1


# Caluculadora

while True:
    print("Bem Vindo à calculadora, se quiser sair digite 'stop' ")
    status = input()
    if "s" in status.lower():
        if "t" in status.lower():
            if "o" in status.lower():
                if "p" in status.lower():
                    break
    else:
        while True:
            valor1 = input("Digite o primeiro número: ")
            valor2 = input("Digite o segundo número: ")
            operador = input("Digite seu operador *, /, +, - : ")
            try:
                valor1 = float(valor1)
                valor2 = float(valor2)
                if operador == "+":
                    print(valor1 + valor2)
                elif operador == "-":
                    print(valor1 - valor2)
                elif operador == "*":
                    print(valor1 * valor2)
                elif operador == "/":
                    print(valor1 / valor2)
                else:
                    print("Operador invalido.")
                    continue
                print()
                print("=" * 20)
                break
            except:
                print("Você não digitou um número, tente novamente.")
                continue






