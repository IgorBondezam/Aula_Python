valor = False

if valor:
    pass    # pass é feito para passar o código, geralmente para execultar algo dps e não der erro
else:
    print("Tchau")

if valor:
    ...    # ... é feito para passar o código, geralmente para execultar algo dps e não der erro
else:
    print("Tchau")

# if valor:                   SE TENTAR EXECULTAR ESSE CODIGO IRÁ DAR ERRO
#                           <--------- POIS NESSA LINHA NÃO HÁ NADA, por isso usamos o pass ou ...
# else:                             para saber se o else execultará certo e dps voltar e escrever o que
#     print("Tchau")                    queremos com o if ou elif
