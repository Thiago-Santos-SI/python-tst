lista1 = ['arara', 'Tv', 'baCia']
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def remove_palavras_com_maiusculas(lista):
    list = []
    for palavra in lista:
        string = ''
        for i in palavra:
            if i not in alfabeto:
                string += i
            else:
                string = ''
                break
        if not string == '':
            list.append(string)
    return list


print(remove_palavras_com_maiusculas(lista1))


