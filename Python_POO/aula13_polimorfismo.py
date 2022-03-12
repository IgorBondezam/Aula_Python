"""
Polimorfismo é o principio que permite que calsses derivadas de uma mesma superclasse tenham métodos iguais(de mesma assisnatura)
mas comportamentos diferentes.
Mesma assinatura = Mesma quantidade e tipo de parâmentros
"""
from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod
    def falar(self, msg):
        pass


class B(A):
    def falar(self, msg):
        print(f"{msg} de B...")


class C(A):
    def falar(self, msg):
        print(f"{msg} de C...")

b = B()
c = C()
b.falar("Aqui")
c.falar("Oiiii")
