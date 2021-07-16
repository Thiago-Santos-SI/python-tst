str = "abradarcx"

def palindromo(list):
    string = ''
    for i in list:
        string += i

    #print('oii', string)

    size = len(string)
    if size == 0:
        return False
    for i in range(0, size // 2):
        if string[i] != string[size - i - 1]:
            return False
    return string

#['a', 'b', 'r', 'a', 'd', 'a', 'r', 'c', 'x']

list = []
for i in str:
    list.append(i)

count = 3
contador = 0
for index in range(4):
    for i in range(len(str) - count):
        isPalindro = palindromo(list)
        if isPalindro != False:
            break
        else:
            list.pop(len(list) - 1)
        print(list)

    list = []
    for i in str:
        list.append(i)
    print('--------------------------------------')

    print('teste', list)
    if contador != 0:
        for i in range(contador + 1):
            print(i)
            list.pop(i)
            print('oi?', list)
    else:
        list.pop(0)

    count += 1
    contador += 1

