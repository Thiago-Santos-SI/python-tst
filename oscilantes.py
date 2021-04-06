numero = int(input())

numeroSTRING = list(str(numero))

list = []

for i in numeroSTRING:
    list.append(int(i))

check = []
algorismos = []

for i in list:
    if len(algorismos) > 0:
        if (i % 2) == 0:
            if (algorismos[0] % 2) == 0:
                check.append(False)
            else:
                check.append(True)
        else:
            if (algorismos[0] % 2) != 0:
                check.append(False)
            else:
                check.append(True)
        del(algorismos[0])
        del(list[0:1])
        print('--->', list)
    else:
        if (i % 2) == 0:
            algorismos.append(i)
        else:
            algorismos.append(i)

print(check)

