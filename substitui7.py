impares, response, number, sete = [], [], [], []

for i in range(0, 101 + 1, 2):
    impares.append(i + 1)

for i in impares:
    for indices in str(i):
        number.append(indices)

    if number[len(number) - 1] == '7':
        sete.append(i)

for i in impares:
    if i > 0 and i not in sete:
        response.append(i)
    if i % 7 == 0:
        response.append('*')
    else:
        for indices in str(i):
            number.append(indices)

            if number[len(number) - 1] == '7':
                response.append('*')
                number = []

print(response)