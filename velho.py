nome1 = input()
dia1 = int(input())
mes1 = int(input())
ano1 = int(input())

nome2 = input()
dia2 = int(input())
mes2 = int(input())
ano2 = int(input())

if ano1 == ano2:
    if mes1 == mes2:
        if dia1 == dia2:
            print('nenhuma')
        else:
            if dia1 < dia2:
                print(nome1)
            else:
                print(nome2)
    else:
        if mes1 < mes2:
            print(nome1)
        else:
            print(nome2)
else:
    if ano1 < ano2:
        print(nome1)
    else:
        print(nome2)
