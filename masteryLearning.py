def descendingOrder(list):
    maiorElement = []
    maior = 0
    contador = 0
    while contador != len(list):
        for i in list:
            if i > maior:
                maior = i
        maiorElement.append(maior)

        newList = []
        for i in list:
            if i != maior:
                newList.append(i)

        list = newList
        maior = 0
    return maiorElement

def sumTwoMajorElements(list):
    maiorMenor = []
    maior = 0
    for i in list:
        if i > maior:
            maior = i
    maiorMenor.append(maior)

    if len(list) == 2:
        maiorMenor.append(list[1])
    else:
        segundoMaior = 0
        for s in list:
            if s != maior:
                if s > segundoMaior:
                    segundoMaior = s
        maiorMenor.append(segundoMaior)

    soma = 0
    for nota in maiorMenor:
        soma += nota
    return soma

list = []
penalizacao = [0.0]
mediaPai = 0
while True:
    n = float(input('Nota? '))
    list.append(int(n))
    if len(list) >= 2:
        soma = sumTwoMajorElements(list)
        media = soma/2
        if media < 6.5:
            print(f'Média: {(soma / 2):.1f} (cursando)')
            print(f'Penalização: {penalizacao[len(penalizacao) - 1]}')
            print()
            sumLast = penalizacao[len(penalizacao) - 1] + 0.5
            penalizacao.append(sumLast)
        elif media >= 6.5:
            mediaPai = media
            print(f'Média: {(soma / 2):.1f} (aprovado)')
            print(f'Penalização: {penalizacao[len(penalizacao) - 1]}')
            print()
            break

validNumbers = []
for i in list:
    if i >= 6:
        validNumbers.append(float(i))

validNumbersSort = descendingOrder(validNumbers)
validNumbersStrnig = ''
for i in validNumbersSort:
    if i == validNumbersSort[len(validNumbersSort) - 1]:
        validNumbersStrnig += str(i)
    else:
        validNumbersStrnig += str(i) + ' ' + 'e' + ' '

print('===')
print(f'Notas válidas: {validNumbersStrnig}')
print(f'Média parcial na unidade: {mediaPai}')
print(f'Penalizações: {float(penalizacao[len(penalizacao) - 1])}')
print(f'Média final na unidade: {mediaPai - 1}')