times = int(input())

list = []
for i in range(times):
    nome = input()
    gols = input()
    list.append(nome)
    list.append(int(gols))

timesList = []
golsList = []
for i in list:
    if type(i) == str:
        timesList.append(i)
    if type(i) == int:
        golsList.append(i)

maior = 0
indice = 0
indiceRepetidos = []
repetidos = []
for i in range(len(golsList)):
    c = golsList[i]
    if c > maior:
        maior = c
        indice = i
    if c == golsList[i-1] or i != len(golsList) - 1 and c == golsList[i+1]:
        repetidos.append(c)
        indiceRepetidos.append(i)

print(repetidos)
if maior in repetidos:
    print(f'Times(s) com melhor ataque ({maior} gols(s)):')
    for i in indiceRepetidos:
        print(f'{timesList[i]}')
else:
    print(f'Times(s) com melhor ataque ({maior} gols(s)):')
    print(f'{timesList[indice]}')

soma = 0
for i in golsList:
    soma += i
print()
print(f'Média de gols marcados: {soma/len(golsList):.1f}')




