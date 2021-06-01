vogais = ['a', 'e', 'i', 'o', 'u', 'u', 'u', 'e']
#vogais = [1, 2, 3, 3, 3]

res = []
for i in range(len(vogais)):
    c = vogais[i]
    if c == vogais[i-1] or i != len(vogais) - 1 and c == vogais[i+1]:
        res.append(c)

print(res)