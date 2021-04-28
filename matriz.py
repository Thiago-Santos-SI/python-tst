def imprime_matriz(matriz):

    colunas = len(matriz[0])

    colunasList = []
    colunasIndice = []
    for i in range(len(matriz)):
        x = matriz[i]
        colunasList.append(len(x))
        colunasIndice.append(i)

    for i in range(len(matriz)):
        for j in range(colunas):
            if j == (colunas - 1):
                print("%d" %matriz[i][j] + 'aa')
            else:
                print("%d" %matriz[i][j] + 'oi', end = " ")
    print()

print(imprime_matriz([[77, 65], [101, 3], [101, 103]]))
