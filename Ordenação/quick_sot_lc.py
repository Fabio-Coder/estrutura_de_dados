def quick_sort_lc(arr):
    if len(arr) <= 1:
        return arr
    m = arr[0]
    return quick_sort_lc([i for i in arr if i < m]) + \
           [i for i in arr if i == m] + \
           quick_sort_lc([i for i in arr if i > m])


def quick_sort_2(l):
    if lista:
        left = [x for x in lista if x < lista[0]]
        right = [x for x in lista if x > lista[0]]
        if len(left) > 1:
            left = quick_sort_2(left)
        if len(right) > 1:
            right = quick_sort_2(right)
        return left + [lista[0]] * lista.count(lista[0]) + right
    return []


if __name__ == '__main__':
    lista = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(quick_sort_lc(lista))
    print(lista)
    print(quick_sort_2(lista))
