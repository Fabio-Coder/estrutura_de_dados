from Analise_de_complexidade.cronometro import cronometro, cronometro_ns


def bubble_sort(lista):
    """
    Recebe uma lista de inteiros

    :param lista:
    :return:
    """
    sentinela = False
    while not sentinela:
        sentinela = True
        for i in range(len(lista)-1):
            if i < len(lista):
                if lista[i] > lista[i+1]:
                    sentinela = False
                    lista[i],lista[i+1]=lista[i+1],lista[i]
    return lista
