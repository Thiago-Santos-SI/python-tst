valores = [1,2,3,4,436,6,7,8,9,10,434]

maior = 0
for i in valores:
    if i > maior:
        maior = i

segundoMaior = 0
for s in valores:
    if s != maior:
        if s > segundoMaior:
            segundoMaior = s


valore = [[77, 65], [101, 3], [101, 103]]

colunas = []
colunasIndice = []
for i in range(len(valore)):
    x = valore[i]
    colunas.append(len(x))
    colunasIndice.append(i)

print(colunas)
print(colunasIndice)

