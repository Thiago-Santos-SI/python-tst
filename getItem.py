valores = [18, 22, 73, 32, 19, 21, 43]

indices = [3, 4, 8, 1]


def index_exist(element, list):
    for index in range(len(list)):
        if element == index:
            return True


def get_items(valores, indices):
    newList = []
    for index in indices:
        if index_exist(index, valores):
            for i in range(len(valores)):
                x = valores[i]
                if i == index:
                    newList.append(x)
        else:
            newList.append(None)
    return newList


print(get_items(valores, indices))
