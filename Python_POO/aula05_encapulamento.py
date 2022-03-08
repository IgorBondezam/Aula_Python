"""
!= de python - public, protected, private

para python
_     ( = protected)
__    ( = privado) proibe alo q acesse de fora da classe
"""


class BaseDate:
    def __init__(self):
     #  self.dados = {}  # coração do codigo, q é publico, mas se eu coloco um _ antes, o python ira recomendar n acessar esse atributo
     #   self._dados = {}  # dois __ é o privado mais forte
        self.__dados = {}

    def inserir_cliente(self, id, nome):
        if "clientes" not in self.__dados:
            self.__dados["clientes"] = {id: nome}
        else:
            self.__dados["clientes"].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados["clientes"].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados["clientes"][id]


base = BaseDate()
base.inserir_cliente(1, "Otavio")
base.inserir_cliente(2, "Miranda")
base.inserir_cliente(3, "Joana")
base.apaga_cliente(2)
base.lista_clientes()
