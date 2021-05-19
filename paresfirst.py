def pares_primeiro(lista):
    primos = []
    pares = []
    for i in lista:
        if i % 2:
            primos.append(i)
        else:
            pares.append(i)

    for i in primos:
        pares.append(i)

    return pares


lista = [3, 6, 4, 0, 7, 8, 11]
assert pares_primeiro(lista) == [6, 4, 0, 8, 3, 7, 11]
assert lista == [3, 6, 4, 0, 7, 8, 11]