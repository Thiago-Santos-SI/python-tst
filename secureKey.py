chave = input()

vogais = ['a', 'e', 'i', 'o', 'u']

achouVogal = []
achouVogalposicao = []
for v in range(len(chave)):
    c = chave[v]
    for i in vogais:
        if c == i:
            achouVogal.append(c)
            achouVogalposicao.append(v)

chaveList = []
for c in chave:
    chaveList.append(c)

consecutivos = []
posicoesConsecutivos = []
for i in range(len(chaveList)):
    c = chaveList[i]
    if c == chaveList[i - 1] or i != len(chaveList) - 1 and c == chaveList[i + 1]:
        consecutivos.append(c)
        posicoesConsecutivos.append(i)


if len(achouVogal) > 0 and len(achouVogal) >= 5:
    if len(consecutivos) > 0 and len(consecutivos) == 3:
        if achouVogalposicao[0] < posicoesConsecutivos[0]:
            if achouVogalposicao[1] < posicoesConsecutivos[1]:
                if achouVogalposicao[2] < posicoesConsecutivos[2]:
                    if len(achouVogal) > 6:
                        print(f'Chave insegura. 6 vogais.')
                    else:
                        print(f'Chave insegura. {len(achouVogal)} vogais.')
                else:
                    print(f'Chave insegura. {len(consecutivos)} caracteres consecutivos iguais.')
    else:
        if len(achouVogal) > 6:
            print(f'Chave insegura. 6 vogais.')
        else:
            print(f'Chave insegura. {len(achouVogal)} vogais.')
else:
    if len(consecutivos) > 0 and len(consecutivos) == 3:
        print(f'Chave insegura. {len(consecutivos)} caracteres consecutivos iguais.')
    else:
        print(f'Chave segura!')