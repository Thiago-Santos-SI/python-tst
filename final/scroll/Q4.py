def scroll(m):
    size = len(m)
    for i in range(1, size):
        aux = m[i]
        m[i - 1] = aux
    m[size - 1] = [0] * len(m[size - 1])
    return m


m = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16],
     [17, 18, 19, 20]]

scroll(m)

assert m == [[5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16],
             [17, 18, 19, 20],
             [0, 0, 0, 0]]

