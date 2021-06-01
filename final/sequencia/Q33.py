def tem123plus(l):
    if len(l) == 0:
        return -1
    for i in range(len(l)):
        if l[i] == 1:
            index1 = i
            index2 = 0
            for j in range(index1 + 1, len(l)):
                if l[j] == 2:
                    index2 = j
                    break
                elif j == len(l) + 1:
                    return -1
            for k in range(index2 + 1, len(l)):
                if l[k] == 3:
                    return index1
                if j == len(l) - 2:
                    return -1
        if i == len(l) - 1:
            return -1


assert tem123plus([3, 2, 1, 2, 3]) == 2
assert tem123plus([4, 1, 1, 1, 4, 2, 3]) == 1
assert tem123plus([1, 2, 2, 3]) == 0
assert tem123plus([1, 2, 2, 4]) == -1
