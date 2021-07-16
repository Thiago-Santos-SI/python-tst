str = 'abracecars'
Input = "hhellosannasmita"


def palindromo(list):
    string = ''
    for i in list:
        string += i

    #print('oii', string)

    size = len(string)
    if size == 0:
        return False
    for i in range(0, size // 2):
        if string[i] != string[size - i - 1]:
            return False
    return string


def teste(str):
    list = []
    for i in str:
        list.append(i)
    for i in range(len(list)):
        if list[1] != list[len(list) - 2]:
            list.pop(0)
            #list.pop(len(list) - 1)
        print(list[1], ' = ', list[len(list) - 2])
        print(list)
        isPalindromo = palindromo(list)
        if isPalindromo != False:
            return isPalindromo
        else:
            list.pop(len(list) - 1)
            isPalindromo2 = palindromo(list)
            if isPalindromo2 != False:
                return isPalindromo


print(teste(Input))
