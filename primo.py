n = int(input())

if n % 7 == 0:
    prim = 7
elif n % 5 == 0:
    prim = 5
elif n % 3 == 0:
    prim = 3
elif n % 2 == 0:
    prim = 2
else:
    prim = False

if prim:
    times = n / prim
    res = times * prim
    print(f"{prim} * {times:.0f} = {res:.0f}")
else:
    print(f"{n} não tem fatores primos menores que 10")