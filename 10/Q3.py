lista = [("Pedro", 1), ("Tito", -1), ("Zeca", 1), ("Lucca", -1), ("Mirna", 0)]
lista2 = [("Tito", -1), ("Lucca", -1), ("Mirna", 0), ("Pedro",1), ("Zeca", 1)]

count = 0
for i in lista[::-1]:
    if count != len(lista):
        lista[count] = i
    count += 1

print(lista)

for index in range(len(lista)):
    i = lista[index]
    if i[1] == 1:
        lista.pop(index)
        lista.append(i)

for index in range(len(lista)):
    i = lista[index]
    if i[1] == 0:
        lista.pop(index)
        lista.append(i)

for index in range(len(lista)):
    i = lista[index]
    if i[1] == 1:
        lista.pop(index)
        lista.append(i)


print(lista)

