vogais = [1, 2, 3, 2, 3, 5, 3]


def igual(element):
    return element == 3


def filter(list):
    result = []

    def igual(element):
        return element == 3

    for i in list:
        if igual(i):
            result.append(i)

    return result


list = [0, 1, 2, 3, 4]


def reducer(accumulator, currentValue):
    return accumulator + currentValue


def reduce(arr, reducex):
    accumulator = arr[0]

    i = 0
    while i < len(arr):
        accumulator = reducex(accumulator, arr[i])
        i += 1

    return accumulator


print(reduce(list, reducer()))


def my_reduce(f, *args):
    if len(args) == 0:
        return None
    result = args[0]
    for i in range(1, len(args)):
        result = f(result, args[i])
    return result
