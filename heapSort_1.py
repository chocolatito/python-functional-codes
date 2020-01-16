import random

"""
MAXIMO UNA LISTA DE 1000 ELEMENTOS
"""


def float_element(l, i):
    if (i > 1 and l[i-1] >= l[(i//2)-1]):
        return float_element(change(l, (i//2)-1, i-1), (i//2))
    else:
        if l[0] >= l[1]:
            return l
        else:
            return l[1:2] + l[0:1] + l[2:]


def change(l, i, j):
    if (i < j):
        return(l[:i] + l[j:j+1] + l[i+1:j] + l[i:i+1] + l[j+1:])
    else:
        print('ERROR EN LOS PARAMETROS i = {0} >= j = {1}'.format(i, j,))


def build_heap(l, index):
    # print('Index = {0} , l = {1}'.format(index, l))
    if len(l) == 1:
        return l
    else:
        if index == 0:
            return l
        else:
            return build_heap(float_element(l, index), index-1)


def extrac_elements(l, n):
    if n == 1:
        return l
    else:
        return l[0:1] + extrac_elements(build_heap(l[1:], n-1), n-1)


def heapSort(l, n):
    if n == 1:
        return l
    else:
        return extrac_elements(build_heap(l, n), n)


lista = random.sample(range(0, 1000), 900)
# print(lista)
# print(lista[1:])
heapSort(lista, len(lista))
