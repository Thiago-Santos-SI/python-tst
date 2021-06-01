def adiciona_item(item, lista):
    lista.append(item)

    for i in range(len(lista)):
        already_sorted = True
        for j in range(len(lista) - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                already_sorted = False
        if already_sorted:
            break

    return lista

lista = ['acucar', 'leite', 'paes', 'queijo']
adiciona_item('cafe', lista)
assert lista == ['acucar', 'cafe', 'leite', 'paes', 'queijo']
print(lista)