
def float_element(l, i):
    if (i > 1 and l[i-1] >= l[(i//2)-1]):
        return float_element(change(l, (i//2)-1, i-1), (i//2))
    else:
        return l


def change(l, i, j):
    return(l[:i] + [l[j]] + l[i+1:j] + [l[i]] + l[j+1:])


def build_heap(l, index):
    if index == 2:
        if l[0] >= l[1]:
            return l
        else:
            return l[::-1][2:] + l[2:]
    else:
        return build_heap(float_element(l, index), index-1)


def extract_elements(l, n):
    # print("lista {0} rango {1}".format(l, n))
    if n < 3:
        if l[0] > l[1]:
            return l
        else:
            return l.reverse()
    else:
        print(l)
        print(l[:1], l[n-1:]+l[1:n-1], n, n-1)
        return (l[:1]
                + extract_elements(
                build_heap(l[n-1:]+l[1:n-1], n-1),
                n-1))


lista = [0, 23, 11, 1, 4, 2, 1, 3]
#       [2, 4, 3, 0, 23, 11, 0, 3, 4, 2, 1, 1] list(range(5))
print(lista)
art = build_heap(lista, len(lista))
print(art)
# print(extract_elements(art, len(art)))

# change(change([1, 2, 3, 4, 5], 1, 4), 0, 1)
# 12,
# 11, 6, 0
# 10, 9, 8
# [12, 10, 11, 8, 9, 0, 6, 7, 3, 1, 4, 2, 5]
