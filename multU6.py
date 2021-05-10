
#numeros = ['joao', 'thiago']


def multipla_lista1(n, lista):
    newList = []
    for i in lista:
        if type(i) == int:
            contador = 0
            for indice in range(n):
                contador += i
            newList.append(contador)
        else:
            for x in range(n):
                newList.append(i)

    return newList

numeros = [2, 3, 4, 6,'thiago', 7]

nomes = ['joao', 'pedro']

def multipla_lista(n, lista):
    newList = []
    if n == 0:
        return newList
    else:
        for i in lista:
            newList.append(i)

        for indice in range(n-1):
            for i in lista:
                newList.append(i)
        return newList


print(multipla_lista(2, nomes))