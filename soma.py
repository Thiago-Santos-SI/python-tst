import math

c1 = float(input("Medida do Cateto 1? "))
c2 = float(input("Medida do Cateto 2? "))

hip = math.sqrt((c1 * c1) + (c2 * c2))

print("Medida da Hipotenusa:", "%.2f" % hip)

