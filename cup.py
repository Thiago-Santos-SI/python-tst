chave = input()

vogais = ['a', 'e', 'i', 'o', 'u']

res = []
for c in chave:
    for i in vogais:
        if c == i:
            res.append(c)

if len(res) > 0 and len(res) >= 5:
    print(f'Chave insegura. {len(res)} vogais.')
else:
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

    if len(consecutivos) > 0:
        print(f'Chave insegura. {len(consecutivos)} caracteres consecutivos iguais.')
    else:
        print(f'Chave segura!')

print(consecutivos)
print(posicoesConsecutivos)
