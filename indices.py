str1 = str(input())
str2 = str(input())



list = []
equal = []
check = []
'ola mundo'
'aso'

for char in range(len(str2)):
    c = str2[char]
    for i in range(len(str1)):
        if len(equal) == 1:
            #quer dizer q ainda estamos no mesmo indice pai
            equal.append(char)
        if len(equal) == 0:
            #quer dizer q nenhum indice foi marcado
            equal.append(char)
        e = str1[i]
        if c == e:
            if len(equal) == 1:
                check.append(True)
                list.append(i)
                if len(check) == 2:
                    print(*list)
                else:
                    print(i)

    list = []
    equal = []
    check = []

