chave = input()

vogais = ['a', 'e', 'i', 'o', 'u']

res = []
for c in chave:
    for i in vogais:
        if c == i:
            res.append(c)

if len(res) > 0:
    print(f'Chave insegura. {len(res)} vogais.')
else:
    chaveList = []
    for c in chave:
        chaveList.append(c)
    res = []
    for i in range(len(chaveList)):
        c = chaveList[i]
        if c == chaveList[i - 1] or i != len(chaveList) - 1 and c == chaveList[i + 1]:
            res.append(c)
    print(f'Chave insegura. {len(res)} caracteres consecutivos iguais.')
