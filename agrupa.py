seq = [6, 15, 12, 6, 8, 3, 25, 14, 1, 10, 7]
seq1 = [15, 25, 10, 6, 12, 6, 8, 3, 14, 1, 7]

thiago azul
isaias vermelho
lucas verde
tata vermelho
dodo laranja
fim

def agrupa_multiplos(seq, k):
    noDivivel = []
    newList = []
    for i in seq:
        if i % k == 0:
            newList.append(i)
        else:
            noDivivel.append(i)

    for i in noDivivel:
        newList.append(i)

    return newList


print(agrupa_multiplos(seq1, 2))

