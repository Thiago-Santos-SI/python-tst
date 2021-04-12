n = int(input())

menor = []
for i in range(10):
    n_children = int(input())
    if n > n_children:
        menor.append(n_children)

somador_contador = 0
for i in menor:
    somador_contador += i

print(f'menores = {len(menor)}')
print(f'soma = {somador_contador}')