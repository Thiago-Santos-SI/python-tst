n = int(input())

list = []
for i in range(n):
    string = input()
    sequence = string.split()
    soma = 0
    for i in sequence:
        soma += int(i)
    if soma == 0:
        list.append(soma)

print(len(list))