list = []
while True:
    entrance = input()
    if entrance == '---':
        break
    else:
        elements = entrance.split(',')
        element = {
            'valor': int(float(elements[0])),
            'tamanho': int(elements[1]),
            'conforto': int(elements[2]),
            'hotel': elements[3],
        }
        list.append(element)


while True:
    entrance = input()
    if entrance == 'fim':
        break
    elif entrance == 'valor':
        valores = [v['valor'] for v in list]
        menor = 100000
        for i in valores:
            if i < menor:
                menor = i

        encontrados = [p for p in list if p['valor'] == menor]
        print(encontrados[0]['hotel'])
    elif entrance == '1':
        print()
    elif entrance == '2':
        print()


#print(list)
'2000.0,1,16,h1 - 4000.0,4,7,h2 - 1900.0,6,23,h3'
#'[{'valor': 2000.0, 'tamanho': 1, 'conforto': 16, 'hotel': 'h1'}, {'valor': 4000.0, 'tamanho': 4, 'conforto': 7, 'hotel': 'h2'}, {'valor': 1900.0, 'tamanho': 6, 'conforto': 23, 'hotel': 'h3'}]'