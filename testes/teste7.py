x = ['b', 'r', 'a', 'd', 'a']


contador = 0
for i in range(len(x)):
    x.pop(contador)
    contador += 1
    print(x)
    if contador == len(x):
        break
