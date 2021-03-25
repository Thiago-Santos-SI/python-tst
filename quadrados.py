x = int(input())
y = int(input())

if x > y:
    print("---")
else:
    for i in range(x, y+1):
        print(f'{i} {i*i}')