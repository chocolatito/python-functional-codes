def quicksort_Imperative(lista):
    """ Method in imperative paradigm
    When 'lista' is a list"""
    if len(lista) <= 1:
        return lista
    else:
        pivot = lista[0]
        i = 0
        for j in range(len(lista)-1):
            if lista[j+1] < pivot:
                lista[j+1], lista[i+1] = lista[i+1], lista[j+1]
                i += 1
        lista[0], lista[i] = lista[i], lista[0]
        left_part = quicksort_Imperative(lista[:i])
        right_part = quicksort_Imperative(lista[i+1:])
        return left_part + [lista[i]] + right_part


def quicksort_Funct_V1(lista):
    """ Method in functional paradigm
    When 'lista' is a list"""
    if len(lista) < 2:
        return lista
    else:
        left_part = [i for i in lista[1:] if i <= lista[0]]
        right_part = [i for i in lista[1:] if i > lista[0]]
        return quicksort_Funct_V1(left_part) + lista[:1] + quicksort_Funct_V1(right_part)

# _____________________________________________________________________________
# ____________________________________________________________________>


def quicksort_Funct_V2(l):
    """ Method quicksort in functional paradigm
    without assignment.
    When 'l' is a list"""
    if len(l) < 2:
        return l
    else:
        return (quicksort_Funct_V2([i for i in l[1:] if i <= l[0]])
                + l[:1]
                + quicksort_Funct_V2([i for i in l[1:] if i > l[0]]))


def left_part(lista):
    return [i for i in lista[1:] if i <= lista[0]]


def right_part(lista):
    return [i for i in lista[1:] if i > lista[0]]


print(quicksort_Funct_V2([9, 8, 6, 7, 5, 4, 32, 1, 0]))
