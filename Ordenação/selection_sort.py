def selection_sort(lista):
    atual = 0
    novo = 0
    sentinela = False

    while not sentinela:
        sentinela = True
        for i in range(len(lista)):
            atual = lista[i]
            for j in range(i, len(lista)):
                novo = lista[j]
                if novo < atual:
                    lista[i], lista[j] = lista[j], lista[i]
                    sentinela = False
    return lista
