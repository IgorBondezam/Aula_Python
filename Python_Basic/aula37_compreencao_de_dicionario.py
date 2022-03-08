
l1 = [
    ("chave", "valor"),
    ("chave2", "valor2"),
]

d1 = {x: y*2 for x, y in l1}
print(d1)

d1 = {f"chave_{x}": x**2 for x in range(5)}
print(d1)