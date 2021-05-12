lista = []
while True:
    sequence = input()
    if sequence == 'fim':
        break
    else:
        palavras = sequence.split()
        maior = 0
        palavra = ''
        for i in palavras:
            if len(i) > maior:
                maior = len(i)
                palavra = i
        lista.append(palavra)

print(lista)

maior = 0
palavra = ''
index = 0
for i in range(len(lista)):
    indice = lista[i]
    if len(indice) > maior:
        maior = len(indice)
        palavra = indice
        index = i+1

print(f'Frase {index}: {palavra}')
