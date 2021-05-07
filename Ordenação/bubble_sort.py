def bubble_sort(lista):
    sentinela = False
    while not sentinela:
        sentinela = True
        for i in range(len(lista) - 1):
            if i < len(lista):
                if lista[i] > lista[i + 1]:
                    sentinela = False
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
    return lista
