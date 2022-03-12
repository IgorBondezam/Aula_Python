class A:
    def falar(self):
        print("Falando... Estou em A.")


class B(A):
    def falar(self):
        print("Falando... Estou em B.")


class C(A):
    def falar(self):
        print("Falando... Estou em C.")


class D(B,
        C):  # Vai fazer a pesquisa da esquerda para a direita, se n encontrar em B vai procurar em C, se n achar vai procurar em A.
    pass


# d = D()
# d.falar()


# EXEMPLO CLASS MIXING


class Eletronico:
    def __init__(self, nome):
        self._nome = nome
        self._ligado = False

    def ligar(self):
        if self._ligado:
            return
        self._ligado = True

    def desligar(self):
        if not self._ligado:
            return
        self._ligado = False


class LogMixin:
    @staticmethod
    def write(msg):
        with open("log.log", "a+") as f:
            f.write(msg)
            f.write("\n")

    def log_info(self, msg):
        self.write(f"INFO - {msg}")

    def log_error(self, msg):
        self.write(f"ERROR - {msg}")


class Smartfone(Eletronico, LogMixin):
    def __init__(self, nome):
        super().__init__(nome)
        self._conectado = False

    def conectar(self):
        if not self._ligado:
            error = f"Ligue o {self._nome} primeiro"
            print(error)
            self.log_error(error)
            return
        if self._conectado:
            error = f"{self._nome} Já está conectado"
            print(error)
            self.log_error(error)
            return
        info = "Aparelho conectado."
        print(info)
        self.log_info(info)
        self._conectado = True

    def desconectar(self):
        if not self._ligado:
            error = f"Ligue o {self._nome} primeiro"
            print(error)
            self.log_error(error)
            return
        if self._conectado:
            self._conectado = False
            info = "Aparelho desconectado."
            print(info)
            self.log_info(info)
            return
        error = "Aparelho já está desconectado."
        print(error)
        self.log_error(error)





telefone = Smartfone("Samsung")
telefone.conectar()
telefone.ligar()
telefone.conectar()
telefone.desconectar()
telefone.desconectar()
telefone.conectar()
telefone.desligar()
telefone.conectar()
telefone.desconectar()
