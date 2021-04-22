def somaMaioresElementos(list):
    maiorMenor = []
    maior = 0
    for i in list:
        if i > maior:
            maior = i
    maiorMenor.append(maior)
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
penalizacao = [0]
while True:
    n = input('Nota? ')
    list.append(int(n))
    if len(list) >= 2:
        soma = somaMaioresElementos(list)
        if soma/2 < 6.5:
            print(f'Média: {(soma / 2):.1f} (cursando)')
            print(penalizacao)
            print(f'Penalização: {penalizacao[len(penalizacao) - 1]}')
            sumLast = penalizacao[len(penalizacao) - 1] + 0.5
            penalizacao.append(sumLast)
        elif soma/2 >= 6.5:
            print(f'Média: {(soma / 2):.1f} (aprovado)')
            print(f'Penalização: {penalizacao[len(penalizacao) - 1]}')
            break
