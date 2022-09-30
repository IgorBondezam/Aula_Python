"""class Arquivo:
    def __init__(self, arquivo, modo):
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        return self.arquivo

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.arquivo.close()
        print(exc_tb, exc_type, exc_val)
        return True

with Arquivo("abc.txt", "w") as arquivo:
    arquivo.write("Alguma coisa")"""

from contextlib import contextmanager

@contextmanager
def abrir_arquivo(arquivo, modo):
    try:
        print("abrindo arquivo")
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print("fechando arquivo")
        arquivo.close()

with abrir_arquivo("abc.txt", "w") as arquivo:
    arquivo.write("linha 1\n")
    arquivo.write("linha 2\n")
    arquivo.write("linha 3\n")
