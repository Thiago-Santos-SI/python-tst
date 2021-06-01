fila = ['1 Andre', '1 Antonio', '2 Bianca', '2 Carlos', '3 Claudia']
#list = [['1 Andre','2 Carlos'],['1 Antonio', '2 Claudia'], ['1 Bianca']]

def safe_div(x,y):
    if y == 0:
        return 0
    return x / y

count = 1
list = []
matriz = []
for index in range(len(fila)):
    i = fila[index]
    print(count, index)
    if count == index or safe_div(count, index) == index:
        list.append(i)
    count += 3
matriz.append(list)

print(matriz)
























def organiza_fila(fila, n):
    count = 0
    list = []
    matriz = []
    for index in range(len(fila)):
        i = fila[index]
        if count == index or count / n == n:
            print('oi')
            list.append(i)
        count += n