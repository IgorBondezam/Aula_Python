try:
    print("a")
    print(a)

except NameError as erro:  # Especifiquei qual erro é
    print("error", erro)
except Exception as erro:  # Para todos os tipos de erro
    print("Ocorreu um erro")
else:  # Se nada der errado, vai execultar isso
    pass
    print("Else")
finally:  # Sempre será execultado, mesmo com erro
    a = "Olá mundo"
    print(a)

