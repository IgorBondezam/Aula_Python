import shutil
from zipfile import ZipFile


def EscreveArquivo():
    arquivo = open("NovoArquivo.txt", "w+")

    arquivo.write("Linha gerada com a funçao 'EscreveArquivo' \r\n")
    arquivo.close()


EscreveArquivo()


def AlteraArquivo():
    arquivo = open("NovoArquivo.txt", "a+")

    arquivo.write("Linha gerada com a funçao 'AlteraArquivo' \r\n")
    arquivo.close()

AlteraArquivo()

def leituraArquivo():
    arquivo = open("NovoArquivo.txt", "r")
    if(arquivo.mode == "r"):
        coteudo = arquivo.read()
        print(coteudo)

    arquivo.close()

leituraArquivo()


def leituraArquivoGrande():
    arquivo = open("NovoArquivo.txt", "r")
    if(arquivo.mode == "r"):
        coteudoTotal = arquivo.readlines()

        for conteudo in coteudoTotal:
            print(conteudo)

    arquivo.close()

leituraArquivoGrande()

import os
from os import path
import time


def DadosArquivo():
    ArquivoExiste = path.exists("NovoArquivo.txt")
    ehDiretorio = path.isdir("NovoArquivo.txt")
    pathArquivo = path.realpath("NovoArquivo.txt")
    pathRelativo = path.relpath("NovoArquivo.txt")
    dataCriacao = time.ctime(path.getctime("NovoArquivo.txt"))
    dataModificacao = time.ctime(path.getmtime("NovoArquivo.txt"))

    print(ArquivoExiste, ehDiretorio, pathArquivo, pathRelativo, dataCriacao, dataModificacao )

DadosArquivo()


def copiaArquivo():
    if path.exists("NovoArquivo.txt"):
        pathAtual = path.relpath("NovoArquivo.txt")
        novoPath = pathAtual + ".bkp"
        shutil.copy(pathAtual, novoPath)

        shutil.copystat(pathAtual, novoPath)

copiaArquivo()


def renomearArquivo():
    if path.exists("NovoArquivo.txt.bkp"):
        os.rename("NovoArquivo.txt.bkp", "ArquivoAlterado.txt")

renomearArquivo()


def CriaZipModo1():
    shutil.make_archive("ArquivoCompactado", "zip", "C:\\cursopython\\aula_basica_python\\Módulo05")

CriaZipModo1()


def CriaZipModo2():
    with ZipFile("ArquivoZipModo2.zip", "w") as novoZip:

        novoZip.write("NovoArquivo.txt")

CriaZipModo2()

def DeletaArquivo():
    os.remove("ArquivoZipModo2.zip")

DeletaArquivo()