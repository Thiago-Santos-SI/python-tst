def alocacao_aulas(alunos):
    wik = []
    dal = []
    jor = []
    for i in alunos:
        if i[1] == 1 or i[1] == 2 or i[1] == 3:
            wik.append(i[0])
        elif i[1] == 4 or i[1] == 5 or i[1] == 6:
            dal.append(i[0])
        elif i[1] == 7 or i[1] == 8 or i[1] == 9 or i[1] == 10:
            jor.append(i[0])

    list = [wik, dal, jor]
    return list

alunos = [("Maria", 3), ("João", 5), ("Carlos", 1), ("Pedro", 9), ("Ângela", 7)]
assert alocacao_aulas(alunos) == [["Maria", "Carlos"],["João"],["Pedro", "Ângela"]]
assert alunos == [("Maria", 3), ("João", 5), ("Carlos", 1), ("Pedro", 9), ("Ângela", 7)]
