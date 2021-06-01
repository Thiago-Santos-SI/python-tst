list = []
recusadas = []
while True:
    soma = 0
    for i in list:
        soma += i
    if soma >= 60:
        break
    sequence = int(input())
    if sequence > 10:
        recusadas.append(sequence)
    else:
        list.append(sequence)

print(f'Rejeitadas = {len(recusadas)}')
print('Fim de semana!')



