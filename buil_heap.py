import random


def float_element(l, i):
    if (i > 1 and l[i-1] >= l[(i//2)-1]):
        return float_element(change(l, (i//2)-1, i-1), (i//2))
    else:
        return l


def change(l, i, j):
    if (i < j):
        return(l[:i] + l[j:j+1] + l[i+1:j] + l[i:i+1] + l[j+1:])
    else:
        print('ERROR EN LOS PARAMETROS i = {0} >= j = {1}'.format(i, j,))


def build_heap(l, index):
    # print('Index = {0} , l = {1}'.format(index, l))
    if index == 1:
        if l[0] >= l[1]:
            return l
        else:
            return l[1:2] + l[0:1] + l[2:]
    else:
        return build_heap(float_element(l, index), index-1)


lista = random.sample(range(1, 20), 19)
print(lista)
print(build_heap(lista, len(lista)))
