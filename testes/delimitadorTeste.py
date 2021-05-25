# a = testando = ['test' 'and']

def put_space(frase, delimitador):
    list = []
    if delimitador != ' ':
        for i in frase:
            list.append(i)
        list.append(' ')
        string = ''
        for i in list:
            string += i
        return string
    else:
        return frase


def split(frase, delimitador):
    list = []
    string = ''

    frase = put_space(frase, delimitador)

    for x in range(len(frase)):
        i = frase[x]
        if i != delimitador and i != frase[len(frase) - 1]:
            string += i
        else:
            list.append(string)
            string = ''
    return list


print(split('teste de fidelidade', 'e'))
