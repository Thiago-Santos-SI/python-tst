palavra = str(input())

vogais = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

vogal = []

if 'a' in palavra or 'A' in palavra or 'e' in palavra or 'E' in palavra or 'i' in palavra or 'I' in palavra or 'o' in palavra or 'O' in palavra or 'u' in palavra or 'U' in palavra:
    for i in list(palavra):
        if i in vogais:
            vogal.append(i)
    print(vogal[0])
else:
    print('-')
