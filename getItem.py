valores = [18, 22, 73, 32, 19, 21, 43]

indices = [3, 4, 8, 1]


def index_exist(element, list):
    for indice in range(len(list)):
        if element == indice:
            return True


def get_items(valores, indices):
    newList = []
    for indice in indices:
        if index_exist(indice, valores):
            for i in range(len(valores)):
                x = valores[i]
                if i == indice:
                    newList.append(x)
        else:
            newList.append(None)
    return newList


print(get_items(valores, indices))
