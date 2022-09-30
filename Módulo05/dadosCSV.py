import csv

with open("clientes.csv", 'r') as arquivo:
    # x = csv.reader(arquivo)
    # for ler in x:
    #     print(ler)
    dados = [x for x in csv.DictReader(arquivo)]
    y = csv.DictReader(arquivo)
    for ler in y:
        print(ler)
        # print(ler['Nome'], ler['Sobrenome'], ler['E-mail'], ler['Telefone'])


with open('cliente2.csv', 'w') as arquivo:
    escreve = csv.writer(arquivo, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_ALL)

    for dado in dados:
        escreve.writerow(
            [
                dado['Nome'],
                dado['Sobrenome'],
                dado['E-mail'],
                dado['Telefone'],
            ]
        )