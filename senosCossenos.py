import math

angulo = float(input())
delta = float(input())
linhas = int(input())

print("|Angulo|   Seno|Cosseno|")

for i in range(linhas):
    angulo_rad = math.radians(angulo)
    seno = math.sin(angulo_rad)
    cosseno = math.cos(angulo_rad)
    print(f"|{angulo:6.1f}|{seno:.5f}|{cosseno:.5f}|")
    angulo = angulo + delta
