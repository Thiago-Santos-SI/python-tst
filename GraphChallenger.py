# Tenha a função GraphChallenge(strArr )
# take strArr que será um conjunto de comprimento três.
# A primeira parte da matriz será uma lista de vértices
# em um gráfico na forma (A,B,C,...), a segunda parte da
# matriz serão as bordas que ligam os vértices na forma (A-B,C-D,...)
# onde cada borda é bidirecional. A última parte da matriz será um conjunto
# de vértices na forma (X,Y,Z,...) e seu programa terá que determinar se o
# conjunto de vértices dado, forma ou não um caminho hamiltoniano no gráfico, o
# que significa que cada vértice no gráfico é visitado apenas uma vez na ordem dada.
# Por exemplo: se strArr é ["(A,B,C,D)","(A-B,A-D,B-D,A-C)","(C,A,D,B)"] então os vértices
# (C,A,D,B) nesta ordem fazem de fato formar um caminho hamiltoniano no gráfico para que
# seu programa deva retornar a corda sim .

# Se, por exemplo, a última parte da matriz foi (D,A,B,C) então isso não forma um caminho
# hamiltoniano, porque uma vez que você chegar a B você não pode chegar a C no gráfico
# sem passar pelos vértices visitados novamente. Aqui o seu programa deve retornar o
# vértice onde o caminho teve que terminar, neste caso o seu programa deve retornar B.
# O gráfico terá pelo menos 2 vértices e todos os vértices do gráfico estarão
# conectados

po = ["(A,B,C,D)", "(A-B,A-D,B-D,A-C)", "(C,A,D,B)"]

strArr = [('A', 'B', 'C', 'D'), ['A-B', 'A-D', 'B-D', 'A-C'], ['C', 'A', 'D', 'B']]

list2 = ['A-B', 'C-D']


def vertex_union(list):
    newList = []
    for index in range(len(list)):
        str = ''
        for i in list[index]:
            if i != '-':
                str += i
        newList.append(str)
    return newList


def path_union(list):
    newList = []
    for index in range(len(list)):
        if list[index] != list[len(list) - 1]:
            var = list[index] + list[index + 1]
            newList.append(var)
    return newList


strArr = [('A', 'B', 'C', 'D'), ['A-B', 'A-D', 'B-D', 'A-C'], ['C', 'A', 'B', 'D']]


def reverseString(text):
    l = list(text)
    l.reverse()
    return ''.join(l)


def GraphChallenge(strArr):
    check = []
    list_vertex_union = vertex_union(strArr[1])
    list_path_union = path_union(strArr[2])
    print(list_path_union)
    print(list_vertex_union)
    for element in list_path_union:
        if element in list_vertex_union or reverseString(element) in list_vertex_union:
            check.append(True)
        else:
            check.append(False)
    if False in check:
        return 'nao'
    else:
        return 'sim'


print(GraphChallenge(strArr))
# print(vertex_union(strArr[1]))


# print(path_union(strArr[2]))
