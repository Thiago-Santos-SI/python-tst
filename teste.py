# listTest = [1, 2, 1, 1, 2, 0, 0, 3, 2]
listTest = []

while True:
    n = input()
    if n == '-':
        break
    else:
        listTest.append(int(n))


def rem_rep(lt):
    l = []
    for i in lt:
        if i not in l:
            l.append(i)
    return l


x = rem_rep(listTest)

res = []
for index in range(len(x)):
    count = 0
    for i in listTest:
        if i == x[index]:
            count += 1
    res.append(count)
    count = 0

count = 0
for i in range(len(x)):
    print(f"{x[count]} repetiu {res[count]} vezes")
    count += 1

print(x)
