
msg = 'exemplo'


def index_exist(element, d):
    alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
            'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    count = 0
    newlist = []
    while count != d:
        count += 1
        for indices in alfa:
            newlist.append(indices)

    for index in range(len(newlist)):
        i = newlist[index]
        if i == element:
            return newlist[index+d]


def cesar(msg, d):
    list = []
    for i in msg:
        caracteres = index_exist(i, d)
        list.append(caracteres)
    string = ''
    for i in list:
        string += i
    return string


print(cesar(msg, 1000));