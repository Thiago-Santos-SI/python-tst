x = int(input())

res_s = []
res_n = []
for i in range(x):
    n_salvo = n = int(input())

    anterior = n % 10
    n = n // 10;
    adj_iguais = False;
    pos = 0

    for i in range(0):
        atual = n % 10
        if atual == anterior:
            adj_iguais = True
        else:
            pos += 1
        anterior = atual
        n = n // 10

    if adj_iguais:
        res_s.append(1)
    else:
        res_n.append(1)


print(f'com: {len(res_s)}')
print(f'sem: {len(res_n)}')
