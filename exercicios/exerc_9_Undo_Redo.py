from time import sleep


def add(lista):
    adicionar_lista = True
    while adicionar_lista:
        adiciona = input("Caso queira sair digite 'sair.'\nO que deseja colocar na sua lista de tarefas? ")
        if not adiciona == 'sair.':
            lista.append(adiciona)
        else:
            break


def listar(lista):
    contar = 1
    print()
    print("Sua lista:")
    for i in lista:
        print(f"    {contar} - {i}")
        contar += 1
    sleep(4)


def desfazer(lista, lista_acao):
    try:
        last_undo = lista.pop()
        lista_acao.append(last_undo)
    except:
        print("Adicione algo à sua lista primeiro.")
        sleep(2)


def refazer(lista, lista_acao):
    try:
        lista.append(lista_acao[-1])
        lista_acao.pop()
    except:
        print("Desfassa algo primeiro.")
        sleep(2)


lista_tarefas = []
lista_undo_redo = []
repet = True
while repet:

    print("-"*50)
    print()
    print("1 - Adicionar tarefa.")
    print("2 - Listar tarefas.")
    print("3 - Desfazer tarefa.")
    print("4 - Refazer tarefa.")
    print("5 - Sair do programa.")
    print()
    print("-"*50)
    print()
    try:
        acao = int(input("Digite algum número para realizar a ação: "))
        if not acao < 6 or not acao > 0:
            print("Digite apenas um dos números alí presente.")
            sleep(3)
            continue
        print()
    except ValueError:
        print("Digite apenas um dos números alí presente.")
        sleep(3)
        continue

    if acao == 1:
            add(lista_tarefas)
    elif acao == 2:
        listar(lista_tarefas)
    elif acao == 3:
        desfazer(lista_tarefas, lista_undo_redo)
        print(lista_undo_redo)
    elif acao == 4:
        refazer(lista_tarefas, lista_undo_redo)
    elif acao == 5:
        certificado = input("Deseja realmente sair do programa? ")
        if certificado.lower() == "sim" or certificado.lower() == "s":
            print("Bye Bye!")
            break
        elif certificado.lower() == "não" or certificado.lower() == "nao" or certificado.lower() == "n":
            continue
        else:
            print("Digite só sim ou não.")
            sleep(2)
            continue
