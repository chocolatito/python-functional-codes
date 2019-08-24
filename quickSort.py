def quicksort_Imperative(lista):
    """ Method in imperative paradigm
    When 'lista' is a list"""
    if len(lista) <=1:
        return lista
    else:
        pivot = lista[0]
        i = 0
        for j in range(len(lista)-1):
            if lista[j+1] < pivot:
                lista[j+1],lista[i+1] = lista[i+1], lista[j+1]
                i += 1
        lista[0],lista[i] = lista[i],lista[0]
        left_part = quicksort_Imperative(lista[:i])
        right_part = quicksort_Imperative(lista[i+1:])
        return left_part + [lista[i]] + right_part


def quickS_Funct_V1(lista):
    """ Method in functional paradigm
    When 'lista' is a list"""
    if len(lista) < 2:
        return lista
    else:
        left_part = [i for i in lista[1:] if i <= lista[0]]
        right_part = [i for i in lista[1:] if i > lista[0]]
        return  quickS_Funct_V1(left_part) + lista[:1] + quickS_Funct_V1(right_part)

#_____________________________________________________________________________
#____________________________________________________________________>

def quickS_Funct_V2(lista):
    """ Method quicksort in functional paradigm
    without assignment.
    When 'lista' is a list"""
    if len(lista) < 2:
        return lista
    else:
        return  quickS_Funct_V2([i for i in lista[1:] if i <= lista[0]]) + lista[:1] + quickS_Funct_V2([i for i in lista[1:] if i > lista[0]])

print(quickS_Funct_V2([1,9,8,6,4,3,2,5,7,1,4]))