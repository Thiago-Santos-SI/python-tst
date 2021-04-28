limite = int(input())

gastos = []
while True:
    sequencia = input()
    if sequencia == 'fim':
        break
    else:
        result = sequencia.split()
        string = ''
        for i in result:
            x = float(i)
            s = str(x)
            string += s + ' '

        soma = 0
        for i in result:
            soma += float(i)

        if soma / len(result) < limite / 2:
            soma = 0
            break
        else:
            somador = 0
            for i in result:
                somador += float(i)
            if somador / len(result) > limite:
                gastos.append(string)
                string = ''

for i in gastos:
    print(i)