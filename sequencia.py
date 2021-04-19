v = int(input())
sequencia = input()

result = sequencia.split()

number = []
for i in result:
    number.append(int(i))

#  [1, 2, 7, 10, 2, 7, 1]

achou = []
for indice in range(len(number)):
    c = number[indice]
    if c == v:
        achou.append(indice)

print(*achou)
