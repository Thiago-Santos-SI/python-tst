def distribui_alunos(turma1, turma2, capacidade):
    list = []
    count = 0
    while count != capacidade + 1:
        if count <= len(turma1) - 1:
            list.append(turma1[count])
        if count <= len(turma2) - 1:
            list.append(turma2[count])
        count += 1

    print(list)
    list1 = []
    list2 = []
    count = 1
    for index in range(len(list)):
        elements = list[index]
        indices = index + 1
        if indices <= capacidade:
            list1.append(elements)
        else:
            print(count)
            if count <= capacidade:
                list2.append(elements)
            count += 1

    matriz = []
    matriz.append(list1)
    matriz.append(list2)

    return matriz


t1 = [10, 38, 87, 22, 25]
t2 = [43, 21, 96, 33, 85, 17, 94]
print(distribui_alunos(t1, t2, 8))

#assert distribui_alunos(t1, t2, 6) == [[10, 43, 38, 21, 87, 96], [22, 33, 25, 85, 17, 94]]