n = int(input())

consoantes = 'bcdfgjklmnpqrstvwxzBCDFGJKLMNPQRSTVWXZ'

consoantesList = list(consoantes)

result = []

list = []
for i in range(n):
    palavra = str(input())
    list.append(palavra)

for i in list:
    if i[0] in consoantesList:
        result.append(i)

print(f"total de palavras: {n}")
print(f"iniciadas por consoantes: {len(result)} ({((len(result)/n)*100):.2f}%)")
