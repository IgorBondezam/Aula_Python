"""
EM PYTHON tudo é um objeto: incluindo classes
MEtaclasses são as "classes" que criam classes
type é uma metaclasse(!!!???)
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        print(name)
        # print(bases)
        # print(namespace)
        if name == "A":
            return type.__new__(mcs, name, bases, namespace)

        if "attr_classes" in namespace:
            del namespace["attr_classes"]

        if "b_fala" not in namespace:
            print(f"Você precisa criar o método b_fala em {name}")
        else:
            if not callable(namespace["b_fala"]):
                print(f"b_fala precisa ser um método em {name}")

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classes = "Valor A"


class B(A):
    attr_classes = "Valor B"


b = B()
print(b.attr_classes)
