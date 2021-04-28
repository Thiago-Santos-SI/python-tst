media_mensal = float(input())

acima = []
abaixo = 0
while True:
    valores = input().split()
    soma  = 0
    if valores[0] == 'fim': break
    for i in range(len(valores)):
        soma += float(valores[i])
    media = soma / len(valores)
    if media > media_mensal:
        acima.append(valores)
    elif media*2 < media_mensal: break
    else:
        abaixo += 1

for lista in acima:
    ultimo = len(lista)-1
    resultado = ''
    ajuste = 0
    for valor in range(len(lista)):
        if valor == 0 and valor != ultimo:
            ajuste = float(lista[valor])
            resultado = resultado + str(ajuste) + " "
        elif valor == ultimo:
            ajuste = float(lista[valor])
            resultado = resultado + str(ajuste)
        else:
            ajuste = float(lista[valor])
            resultado = resultado + str(ajuste) + " "

    if len(resultado) > 0:
        print(resultado)