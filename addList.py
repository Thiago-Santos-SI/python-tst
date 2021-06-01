def meu_in(parametro, lista):
    for c in lista:
        if c == parametro:
            return (True)
    return (False)


def adiciona_item(item, lista):
    lista1 = []
    for neg in lista:
        a = meu_in(item, lista1)
        if not a:
            if ord(item[0]) < ord(neg[0]):
                lista1.append(item)
                lista1.append(neg)
            else:
                lista1.append(neg)
        else:
            lista1.append(neg)
    for i in range(len(lista)):
        lista.pop()
    for c in range(len(lista1)):
        lista.append(lista1[c])

    return lista


lista = ['acucar', 'leite', 'paes', 'queijo']
adiciona_item('cafe', lista)
assert lista == ['acucar', 'cafe', 'leite', 'paes', 'queijo']
