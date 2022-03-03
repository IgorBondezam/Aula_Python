cont = 0
a = 0
b = 10

while cont <= 8:
    print(a, b)
    cont += 1
    a += 1
    b -= 1


for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
