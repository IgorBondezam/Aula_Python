class A:
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)

    def __init__(self):
        print("Init")

    def __call__(self, *args, **kwargs):  # Faz com que a classe possa ser uma função
        print(args, kwargs)

    def __setattr__(self, key, value):  # Faz com que qualquer atributo que n foi criado, seja chamado como (a.key = value)
        print(key, value)

    def __del__(self):  # Vai ser execultado sempre quando o Garbtcolector do python é execultado
        print("Objeto Coletado")

    def __str__(self):  # Execulta a classe como uma string
        return "Essa é a classe q virou uma string"

    def __len__(self):  # Execulta a classe com um len
        return 55

a = A()
a(1, 2, 3, 4, 5, nome="luiz")
a.nome = "Luiz Otávio"
print(a)
print(len(a))
