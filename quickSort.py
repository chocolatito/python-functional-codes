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


def quicksort_Funcional(lista):
    """ Method in functional paradigm
    When 'lista' is a list"""
    if len(lista) < 2:
        return lista
    else:
        left_part = [i for i in lista[1:] if i <= lista[0]]
        right_part = [i for i in lista[1:] if i > lista[0]]
        return quicksort_Funcional(left_part) + lista[:1] + quicksort_Funcional(right_part)

print(quicksort_Funcional([]))