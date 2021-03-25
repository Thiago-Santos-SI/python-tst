nome = str(input("Nome? "))
valor_letra = float(input("Valor da letra (R$)? "))

preco = len(nome) * valor_letra

print(f"Preço final: R$ {preco:.2f}")
