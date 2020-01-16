import random
import time


def quicksort_Imperative(l):
    """ Method in imperative paradigm
    When 'l' is a list"""
    if len(l) <= 1:
        return l
    else:
        pivot = l[0]
        i = 0
        for j in range(len(l)-1):
            if l[j+1] < pivot:
                l[j+1], l[i+1] = l[i+1], l[j+1]
                i += 1
        l[0], l[i] = l[i], l[0]
        left_part = quicksort_Imperative(l[:i])
        right_part = quicksort_Imperative(l[i+1:])
        return left_part + [l[i]] + right_part


def quicksort_Funct_V1(l):
    """ Method in functional paradigm
    When 'l' is a list"""
    if len(l) < 2:
        return l
    else:
        left_part = [i for i in l[1:] if i <= l[0]]
        right_part = [i for i in l[1:] if i > l[0]]
        return quicksort_Funct_V1(left_part) + l[:1] + quicksort_Funct_V1(right_part)

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


# print(quicksort_Funct_V2(random.sample(range(0, 100000), 99999)))
