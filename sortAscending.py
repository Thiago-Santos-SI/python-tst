def sortAscending(list):
    menorElement = []
    menor = 10000
    contador = 0
    while contador != len(list):
        for i in list:
            if i < menor:
                menor = i
        menorElement.append(menor)
        newList = []
        for i in list:
            if i != menor:
                newList.append(i)

        list = newList
        menor = 10000
    return menorElement

valores = [1,2,3,4,436,6,7,235,8,9,10,434, 1000]

print(sortAscending(valores))
