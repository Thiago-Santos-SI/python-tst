# PROG1 - UFCG
# UNIDADE 8 - HOSPITAL DE TRAUMA

def split(frase, delimitador):
    lista = []
    acumulador = ""
    for index in range(len(frase)):
        if frase[index] != delimitador:
            acumulador += frase[index]
        else:
            if acumulador != "":
                lista.append(acumulador)
                acumulador = ""
    if acumulador:
        lista.append(acumulador)

    return lista


def cadastra(fila, nome, prioridade):
    listinha = [nome, prioridade]
    fila.append(listinha)


def resumo():
    for i in range(len(fila) - 1):
        for j in range(i + 1, len(fila)):
            if fila[i][1] < fila[j][1]:
                fila[i], fila[j] = fila[j], fila[i]


fila = []
cont_vermelho = 0
cont_laranja = 0
cont_amarelo = 0
cont_verde = 0
cont_azul = 0
while True:
    entrada = input()
    if entrada == 'fim':
        break

    dados = split(entrada, ' ')

    prioridade = 0
    if dados[1] == 'vermelho':
        prioridade = 4
        cont_vermelho += 1
    elif dados[1] == 'laranja':
        prioridade = 3
        cont_laranja += 1
    elif dados[1] == 'amarelo':
        prioridade = 2
        cont_amarelo += 1
    elif dados[1] == 'verde':
        prioridade = 1
        cont_verde += 1
    elif dados[1] == 'azul':
        prioridade = 0
        cont_azul += 1

    cadastra(fila, dados[0], prioridade)

resumo()
for i in range(len(fila)):
    print(f'{fila[i][0]}')

print('---')
print(f'vermelho: {cont_vermelho}')
print(f'laranja: {cont_laranja}')
print(f'amarelo: {cont_amarelo}')
print(f'verde: {cont_verde}')
print(f'azul: {cont_azul}')
print('---')








