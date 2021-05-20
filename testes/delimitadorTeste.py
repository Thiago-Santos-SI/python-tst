string = 'esse e um bom exemplo'


def split(frase, delimitador):
    string = ''
    list = []
    for index in range(len(frase)):
        i = frase[index]
        print(string)
        if i != ' ':
            string += i
        if index == len(frase) + 1:
            list.append(string)
        else:
            list.append(string)
            string = ''

    return list


print(split('esse e um bom exemplo', 'a'))
