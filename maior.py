
valores = [1,2,3,4,436,6,7,8,9,10,434]
maior = 0
for i in valores:
    if i > maior:
        maior = i

segundoMaior = 0
for s in valores:
    if s != maior:
        if s > segundoMaior:
            segundoMaior = s

print('maior', maior)
print('maior', segundoMaior)