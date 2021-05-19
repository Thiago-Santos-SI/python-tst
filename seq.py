
let = [1]

cont = 0
for i in let:
    if cont == 4:
        break
    else:
        cont += 1
        x = i + i
        let.append(x)

print(*let)
