def remove_repetidos(list):
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

    newListTwo = []

    accumulator = 0
    for i in menorElement:
        if i == accumulator:
            x = None
        else:
            newListTwo.append(i)
            accumulator = i

    return newListTwo


lt = [1, 1, 2, 1, 3, 4, 4, 3, 6, 7, 6, 7, 8, 10, 50, 90, 50]

x = remove_repetidos(lt)
print(x)
