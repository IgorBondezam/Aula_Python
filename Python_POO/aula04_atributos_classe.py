class A:
    vc = 123  # Variavel de classe, q está distribuida para toda a classe

a1 = A()
a2 = A()

a1.vc = 321

print(a1.__dict__)
print(a2.__dict__)
print(A.__dict__)
print(a1.vc)
print(a2.vc)
print(A.vc)

A.vc = 321

print(a1.vc)
print(a2.vc)
print(A.vc)
