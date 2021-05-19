n = int(input())

list = []
for i in range(n):
    entrance = input()
    elements = entrance.split('|')
    element = {
        'valor': int(float(elements[0])),
        'conexões': int(elements[1]),
        'tempo': int(elements[2]),
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
    elif entrance == 'conexões':
        valores = [v['conexões'] for v in list]
        maior = 100000
        for i in valores:
            if i < maior:
                maior = i
        encontrados = [p for p in list if p['conexões'] == maior]
        print(encontrados[0]['hotel'])
    elif entrance == 'tempo':
        valores = [v['tempo'] for v in list]
        maior = 100000
        for i in valores:
            if i < maior:
                maior = i
        encontrados = [p for p in list if p['tempo'] == maior]
        print(encontrados[0]['hotel'])
    elif entrance == 'fim':
        break