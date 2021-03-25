salario_bruto = float(input())
horas_de_trabalho = int(input())
ganhos_por_hora = salario_bruto / horas_de_trabalho

IR = salario_bruto * 0.11
INSS = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salário_liquido = salario_bruto - (IR + INSS + sindicato)
hora_liquida = salário_liquido / horas_de_trabalho

print(f"Salário Bruto =", "%.2f" % salario_bruto)
print(f"Hora Bruta =", "%.2f" % ganhos_por_hora)
print(f"Desconto IR =", "%.2f" % IR)
print(f"Desconto INSS =", "%.2f" % INSS)
print(f"Desconto Sindicato =", "%.2f" % sindicato)
print(f"Salário Líquido =", "%.2f" % hora_liquida)
print(f"Hora Líquida =", "%.2f" % hora_liquida)

