vogais = ['a', 'e', 'i', 'o', 'u', 'u', 'u', 'e']

res = []
for i in range(len(vogais)):
    c = vogais[i]
    if c == vogais[i-1] or i != len(vogais) - 1 and c == vogais[i+1]:
        res.append(c)

print(res)