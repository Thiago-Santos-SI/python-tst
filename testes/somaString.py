numbers = [11, 22, 33]

list = []
for i in numbers:
    numberString = str(i) #11
    soma = 0
    for x in numberString:
        soma += int(x)
    list.append(soma)

print(list)
