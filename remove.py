lista = [1, "Prog1", 3.4, 1]


def meu_in(parametro, lista):
    for i in lista:
        if i == parametro:
            return True
    return False


def remove_ocorrencias(lista, elemento):

    sim = ''

    for i in range(len(lista)-1, -1, -1):
        if lista[i] == elemento:
            lista.pop(i)
            sim = 's'
    if sim == 's':
        return elemento

    return None

lista = [1, "Prog1", 3.4, 1]

print(remove_ocorrencias(lista, 1))
print(lista)