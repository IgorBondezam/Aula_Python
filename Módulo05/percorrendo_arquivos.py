import os

caminho_procura = input("Digite um caminho: ")
termo_procura = input("Digite um termo: ")
contador = 0

def formataTamanho(tamanho):
    base = 1024
    kilo = base
    mega = base**2
    giga = base**3
    tera = base**4
    peta = base**5

    if tamanho < kilo:
        text = "B"
    elif tamanho < mega:
        tamanho /= kilo
        text = "K"
    elif tamanho < giga:
        tamanho /= mega
        text = "M"
    elif tamanho < tera:
        tamanho /= giga
        text = "G"
    elif tamanho < peta:
        tamanho /= tera
        text = "T"

    tamanho = round(tamanho, 2)
    return f'{tamanho}{text}'



for raiz, direstorios, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contador += 1
                caminhoCompleto = os.path.join(raiz, arquivo)
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                tamanho = os.path.getsize(caminhoCompleto)
                print()
                print("=" * 50)
                print(nome_arquivo)
                print("-"*50)

                print("Encontrei o arquivo: ", arquivo)
                print("Encontrei o caminho dele é: ", caminhoCompleto)
                print("Encontrei a extensão: ", ext_arquivo)
                print("Encontrei o Nome: ", nome_arquivo)
                print("Encontrei o tamanho: ", tamanho, "byts")
                print("Encontrei o tamanho: ", formataTamanho(tamanho))
                print()
            except PermissionError as e:
                print("Sem permissões.")
            except FileNotFoundError as e:
                print("Arquivo não encontrado.")
            except Exception as e:
                "Erro."

print()

print(contador, "Arquivo(s) encontrado(s)")
