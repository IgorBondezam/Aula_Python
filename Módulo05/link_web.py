import urllib.request

def ConectaInternet():
    objurl = urllib.request.urlopen("http://www.google.com")

    if objurl.getcode() == 200:
        dados = objurl.read()
        print(dados)

ConectaInternet()

import json_aula

def ManipulaJson():
    endereco = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"
    webURL = urllib.request.urlopen(endereco)

    if (webURL.getcode() == 200):
        dados = webURL.read()
        oJSON = json.loads(dados)

        contagem = oJSON["metadata"]["count"]

        print("contagem:" + str(contagem))

        for local in oJSON["features"]:
            if local["properties"]["place"] == "43 km W of San Antonio de los Cobres, Argentina" :
                print("Encontrado lugar esperical ***********************")
            else:
                print(local["properties"]["place"])

ManipulaJson()


from html.parser import HTMLParser

class meuParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Tag encontrada.")

        if attrs.__len__() > 0:
            for a in attrs:
                print("Valores encontrados: ", a[0], "=", a[1])

    def handle_endtag(self, tag):
        print("Tag de fechamento")

    def handle_comment(self, data):
        print("Comentário encontrado.")

    def handle_data(self, data):
        print("Valores encontrados.")
        if data.isspace():
            print("O valor encontrado é um espaço")
        else:
            print("O valor encontrado é: ", data)


def meuObjeto():
    meuParser1 = meuParser()
    arquivo = open("C:\\cursopython\\aula_basica_python\\Módulo05\\index.html", "r")
    dados = arquivo.read()
    meuParser1.feed(dados)

meuObjeto()



