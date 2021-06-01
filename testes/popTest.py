lista = [("Pedro", 1), ("Tito", -1), ("Zeca", 1), ("Lucca", -1), ("Mirna", 0)]
lista2 = [("Tito", -1), ("Lucca", -1), ("Mirna", 0), ("Pedro",1), ("Zeca", 1)]

count = 0
for i in lista[::-1]:
    if count != len(lista):
        lista[count] = i
    count += 1

print(lista)

