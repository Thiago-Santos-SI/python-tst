def remove_space(lista):
    list = []
    for index in range(len(lista)):
        i = lista[index]
        string = ''
        for x in i:
            if x != ' ':
                string += x
        list.append(string)
    return list


def split2(frase, delimitador):
    lista = []
    token = ''
    for i in range(len(frase)):
        if frase[i] == delimitador:
            if token != '':
                lista.append(token)
                token = ''
        else:
            token += frase[i]

    lista.append(token)

    lista_refatorada = remove_space(lista)
    return lista_refatorada

def split(frase, delimitador):
    list = []
    var = ''
    for i in range(len(frase)):
        if frase[i] != delimitador:
            var += frase[i]
        elif frase[i] == delimitador and frase[i - 1] == delimitador:
            var = ''
        elif frase[i] == delimitador and i != 0:
            list.append(var)
            var = ''
    if frase[len(frase) - 1] != delimitador:
        list.append(var)
    return list


print(split('teeestando', 'e'))


assert split('um exemplo', ' ') == ['um','exemplo']
assert split('testando', 'a') == ['test', 'ndo']
assert split('um exemplo maior',' ') == ['um','exemplo','maior']
assert split('duas,,palavras',',') == ['duas','palavras']