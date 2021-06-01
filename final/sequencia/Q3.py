def tem123plus(li):
    i1 = -1
    tem1, tem2 = False, False
    for i in range(len(li)):
        if li[i] == 1:
            tem1 = True
            if i1 == -1:
                i1 = i
        elif li[i] == 2 and tem1:
            tem2 = True
        elif li[i] == 3 and tem1 and tem2:
            return i1

    return -1


assert tem123plus([3, 2, 1, 2, 3]) == 2
assert tem123plus([4, 1, 1, 1, 4, 2, 3]) == 1
assert tem123plus([1, 2, 2, 3]) == 0
assert tem123plus([1, 2, 2, 4]) == -1
