limite = int(input())

gastos = []
while True:
    sequencia = input()
    if sequencia == '-':
        break
    else:
        result = sequencia.split()
        soma = 0
        for i in result:
            soma += int(i)

        if soma >= limite * 5:
            gastos.append(sequencia)
            break
        else:
            somador = 0
            for i in result:
                somador += int(i)
            if somador > limite:
                gastos.append(sequencia)

for sequencia in gastos:
    result = sequencia.split()
    somador = 0
    string = ''
    for i in result:
        somador += int(i)
        if i == result[len(result) - 1]:
            string += i + ' ' + '=' + ' ' + str(somador)
        else:
            string += i + ' ' + '+' + ' '
    print(string)
    string = ''