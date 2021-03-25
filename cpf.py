cpf = int(input())
cpf1 = int(input())
cpf2 = int(input())

a = cpf // 100
b = cpf % 100
c = cpf // 10
d = cpf % 10
e = c % 10

f = cpf1 // 100
g = cpf1 % 100
h = cpf1 // 10
q = cpf1 % 10
l = h % 10

r = cpf2 // 100
s = cpf2 % 100
t = cpf2 // 10
u = cpf2 % 10
v = t % 10

print(f"{a}-{b}")
print(d+e)
print(f"{f}-{g}")
print(q+l)
print(f"{r}-{s}")
print(u+v)
