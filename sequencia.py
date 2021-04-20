v = int(input())
sequencia = input()

result = sequencia.split()

number = []
for i in result:
    number.append(int(i))

#  [1, 2, 7, 10, 2, 7, 1]

achou = []
naoAchou = []
for indice in range(len(number)):
    c = number[indice]
    if c == v:
        achou.append(indice)
    else:
        naoAchou.append(-1)

if len(naoAchou) == len(number):
    print(-1)
else:
    print(*achou)