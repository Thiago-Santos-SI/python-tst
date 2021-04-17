list = []
soma = 0
while True:
    entrance = input()
    if entrance == 'fim':
        break
    else:
        if entrance == '-':
            list.append(9000)
        else:
            if type(entrance) != str:
                soma += entrance
            else:
                list.append(entrance)

soma = 0
for i in list:
    if type(i) != str:
        soma += i

print(list)



