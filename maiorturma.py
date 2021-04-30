list = []
while True:
    sequencia = input()
    if sequencia == 'fim':
        break
    else:
        result = sequencia.split()
        par = []
        impar = []
        for i in result:
            if int(i) % 2:
                impar.append(i)
            else:
                par.append(i)
        if len(par) > len(impar):
            list.append(sequencia)

print(f'filtradas: {len(list)}')
for i in list:
    print(i)


