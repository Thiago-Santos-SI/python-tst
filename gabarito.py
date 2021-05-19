candidato = ['a', 'b', 'X', 'a', 'c', 'd', 'b', 'a']
gabarito = ['a', 'c', 'd', 'a', 'c', 'b', 'b', 'd']


def gabarita(candidato, gabarito):
    count = 0

    for i in range(len(candidato)):
        if candidato[i] == gabarito[i]:
            count += 1
            candidato[i] = '+' + candidato[i]
        elif candidato[i] == 'X':
            candidato[i] = candidato[i]
        else:
            candidato[i] = '-' + candidato[i]
    return count


def gabarita(candidato, gabarito):
    newList = []
    x = len(candidato)
    print(x)
    contador = 0
    while contador != x:
        if candidato[contador] == gabarito[contador]:
            candidato.append('+')
            newList.append('+')
        else:
            candidato.append('-')
        contador += 1

    print(candidato)
    return len(newList)



print(gabarita(candidato, gabarito))