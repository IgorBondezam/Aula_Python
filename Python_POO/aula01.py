from datetime import  datetime

class Pessoa:   #ignora o self e começa a contar do 2° parametro

    ano_atual = int(datetime.strftime(datetime.now(), "%Y"))  # Essa é uma variavel da classe

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo   # Essas são todas variaveis da instancia
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f"{self.nome} não pode falar comendo.")
            return
        if self.falando:
            print(f"{self.nome} já está falando.")
            return

        print(f"{self.nome} está falando sobre {assunto}.")
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando")
            return
        print(f"{self.nome} parou de falar.")
        self.falando = False

    def comer(self, alimento):
        if self.falando:
            print(f"{self.nome} está falando, ainda não consegue comer.")
            return
        if self.comendo:
            print(f"{self.nome} já está comendo")
            return

        print(f"{self.nome} está comendo {alimento}.")
        self.comendo=True

    def parar_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo.")
            return
        print(f"{self.nome} parou de comer.")
        self.comendo = False

    def ano_nascimento(self):
        return self.ano_atual - self.idade  # Mesmo ela sendo uma variavel da classe, precisa do metodo self

p1 = Pessoa("Luiz", 26)

print(p1.nome)
p1.comer("Maça")
p1.falar("POO")
p1.parar_comer()
p1.comer("melancia")
p1.parar_comer()
p1.falar("POO")
p1.comer("lixia")
p1.parar_falar()
p1.comer("lixia")
p1.falar("POISIA")
p1.parar_falar()
print(p1.ano_atual)
print(p1.ano_nascimento())
