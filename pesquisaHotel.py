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
    elif entrance == 'tamanho':
        valores = [v['tamanho'] for v in list]
        maior = 0
        for i in valores:
            if i > maior:
                maior = i
        encontrados = [p for p in list if p['tamanho'] == maior]
        print(encontrados[0]['hotel'])
    elif entrance == 'conforto':
        valores = [v['conforto'] for v in list]
        maior = 0
        for i in valores:
            if i > maior:
                maior = i
        encontrados = [p for p in list if p['conforto'] == maior]
        print(encontrados[0]['hotel'])
    elif entrance == 'fim':
        break

# teste - '1500.0,1,16,h1 - 4000.0,4,30,h2 - 1900.0,6,23,h3'
