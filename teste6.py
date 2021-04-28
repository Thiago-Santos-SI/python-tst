sequencia = '102 103 104'

result = sequencia.split()

string = ''
for i in result:
    x = float(i)
    s = str(x)
    string += s + ' '

print(string)