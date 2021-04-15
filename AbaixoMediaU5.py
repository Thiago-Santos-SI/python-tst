list = []
n = input()
list.append(int(n))
while n != 'fim':
    n = input()
    if n != 'fim':
        list.append(int(n))

soma = 0
for i in list:
    soma += i

media = soma/len(list)
print(f'{media:.2f}')

for i in range(len(list)):
    indice = list[i]
    if indice < media:
       print(i+1, indice)

maior = 0
for i in list:
    if list['valor'] > maior:
        maior = list[i]
print(maior)