valores = [1, 2, 3, 3, 4, 4, 6, 6, 1, 436, 6, 7, 8, 9, 10, 434]


def not_in(element, list):
    bolean = []
    if len(list) == 0:
        return True
    else:
        for i in list:
            if i == element:
                #se ele entra aqui, ele achou, logo existe e retorna False
                bolean.append(False)
            else:
                # se ele entra aqui, ele nao achou, logo nao existe e retorna True
                bolean.append(True)
        search = 0
        for i in bolean:
            if not i:
                # se existe algum True na lista de boleanos, quer dizer que ele achou em algum momento,
                search = True

        if search:
            return False
        else:
            return True


def meu_in(parametro, lista):
    for i in lista:
        if i == parametro:
            return True
    return False


def rem_rep(list):
    newList = []
    for i in list:
        # if i not in newlist:
        if not_in(i, newList):
            newList.append(i)
    return newList


print(rem_rep(valores))

