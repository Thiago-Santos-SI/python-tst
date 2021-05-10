# vermelho -> laranja -> amarelo -> verde -> azul


def cadastra(fila, nome, prioridade):
    let = ''
    if prioridade == 'vermelho':
        let = 'A vermelho'
    elif prioridade == 'laranja':
        let = 'B laranja'
    elif prioridade == 'amarelo':
        let = 'C amarelo'
    elif prioridade == 'verde':
        let = 'D verde'
    elif prioridade == 'azul':
        let = 'E azul'

    string = let + ' ' + nome

    fila.append(string)

    for indice in range(len(fila)):
        already_sorted = True
        for j in range(len(fila) - indice - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
                already_sorted = False
        if already_sorted:
            break

    newMatriz = []
    for element in fila:
        sequence = element.split()
        newMatriz.append(sequence[len(sequence) - 1])

    return newMatriz


lista = []
while True:
    sequence = input()
    if sequence == 'fim':
        break
    else:
        entrada = sequence.split()
        lista = cadastra(lista, entrada[0], entrada[1])


for i in lista:
    print(i)
