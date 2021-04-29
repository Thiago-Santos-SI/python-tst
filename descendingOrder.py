def descendingOrder(list):
    maiorElement = []
    maior = 0
    contador = 0
    while contador != len(list):
        for i in list:
            if i > maior:
                maior = i
        maiorElement.append(maior)

        newList = []
        for i in list:
            if i != maior:
                newList.append(i)

        list = newList
        maior = 0
    return maiorElement

valores = [1,2,3,4,436,6,7,8,9,10,434, 1000]

print(descendingOrder(valores))