number = []
res = []

n = int(input())

for i in str(n):
    number.append(i)

print(number)
if number[len(number)-1] == 7:
    res.append('sim')

print(res)