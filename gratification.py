n1 = int(input())

if n1 == 1:
    print("Deverá receber em dezembro R$ 25000.00.")
elif n1 == 2:
    print("Deverá receber em dezembro R$ 15000.00.")
elif n1 == 3:
    n2 = int(input())
    g = 235 - n2
    print(f"Valor da gratificação R$ 500.00.")
    if n2 == 0:
        print(f"Deverá receber em dezembro R$ {(8000 + 500):.2f}.")
    else:
        print(f"Deverá receber em dezembro R$ {(8000 + (g * 2)):.2f}.")
elif n1 == 4:
    n2 = int(input())
    g = 235 - n2
    print(f"Valor da gratificação R$ 300.00.")
    if n2 == 0:
        print(f"Deverá receber em dezembro R$ {(5000 + 300):.2f}.")
    else:
        print(f"Deverá receber em dezembro R$ {(5000 + (g * 1)):.2f}.")
elif n1 == 5:
    n2 = int(input())
    g = 235 - n2
    print(f"Valor da gratificação R$ 200.00.")
    if n2 == 0:
        print(f"Deverá receber em dezembro R$ {(2800 + 200):.2f}.")
    else:
        print(f"Deverá receber em dezembro R$ {(2800 + (g * 0.70)):.2f}.")
