peso = float(input())
altura = float(input())
imc = peso / altura ** 2

print(f"IMC = {imc:.1f}")
if (imc < 18.5):
    print(f"Classificação = Magreza")
elif (imc >= 18.5 and imc < 25):
    print(f"Classificação = Saudável")
elif (imc >= 25 and imc < 30):
    print(f"Classificação = Sobrepeso")
elif (imc >= 30):
    print(f"Classificação = Obesidade")