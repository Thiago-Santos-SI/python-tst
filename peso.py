peso = float(input())
altura = float(input())
imc = peso / altura ** 2
x = 24.9 * (altura ** 2)
ganho_perda = peso - x

print(f"IMC atual = ", "%.2f" % imc)
print(f"Peso a ser ganho/perdido = -{ganho_perda:.2f}")

