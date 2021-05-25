lista = [1, 2, 1, 3, 4, -1, -3, 5, -5]


def index_exist(element, lista):
    count = 0
    for i in lista:
        if i == element or i == (element * (-element) / element):
            count += 1
    return count


def lista_so_com_oposto(lista):
    copyList = lista
    list = []
    for i in lista:
        x = index_exist(i, copyList)
        if x >= 2:
            list.append(i)

    count = 0
    while len(lista) != len(list):
        lista.pop(count)
        count += 1

    for i in range(len(lista)):
        lista[i] = list[i]

    return None


print(lista_so_com_oposto(lista))
