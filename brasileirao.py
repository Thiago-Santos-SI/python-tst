TA_pontos = int(input())
TA_vitoria = int(input())
TA_gols = int(input())
TA_gols_sofridos = int(input())
TA_saldo_gols = TA_gols - TA_gols_sofridos

TB_pontos = int(input())
TB_vitoria = int(input())
TB_gols = int(input())
TB_gols_sofridos = int(input())
TB_saldo_gols = TB_gols - TB_gols_sofridos

if TA_pontos == TB_pontos:
    if TA_vitoria == TB_vitoria:
        if TA_saldo_gols == TB_saldo_gols:
            print('Os dois times terminaram empatados.')
        else:
            if TA_saldo_gols > TB_saldo_gols:
                print('O Time A ganhou do Time B.')
            else:
                print('O Time B ganhou do Time A.')
    else:
        if TA_vitoria > TB_vitoria:
            print('O Time A ganhou do Time B.')
        else:
            print('O Time B ganhou do Time A.')
else:
    if TA_pontos > TB_pontos:
        print('O Time A ganhou do Time B.')
    else:
        print('O Time B ganhou do Time A.')