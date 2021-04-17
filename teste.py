
b = ['oi',2,3,4,5,6,7,8,9,10,434]
soma_das_notas = 0

for nota in b:
    if type(nota) != str:
        soma_das_notas += nota


print(soma_das_notas)