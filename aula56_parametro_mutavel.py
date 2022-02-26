def lista_de_clientes(cliente_iteravel, lista = []):
    lista.extend(cliente_iteravel)
    return lista

clientes1 = lista_de_clientes(["João", "Maria", "Eduardo"])
clientes2 = lista_de_clientes(["Marcos", "Jonas", "Zico"])

print(clientes1)
print(clientes2)
