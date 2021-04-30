def remove_multiplos(fator, numeros):
    numbers = []
    eliminados = []

    for i in numeros:
        if i % fator == 0:
            numbers.append(i)
        else:
            eliminados.append(i)
    return numbers

print(remove_multiplos(3, [1,2,3,4,436,6,7,8,9,10,434, 1000]))

