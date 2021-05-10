lista_nomes = ['Manuel', 'Laura', 'Antonio', 'Jasmim', 'Maria', 'Silvia', 'Lu', 'Pancracio', 'Diogo', 'Ricardo',
               'Miguel', 'Andre', 'Anhique']


def adiciona_item(item, lista):
    lista.append(item)

    for i in range(len(lista)):
        already_sorted = True
        for j in range(len(lista) - i - 1):
            print(lista[j])
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                already_sorted = False
        if already_sorted:
            break

    return lista


lista_ordenada = adiciona_item('Macarrao', lista_nomes)

print(lista_ordenada)
