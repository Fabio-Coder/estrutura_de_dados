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

if __name__ == '__main__':
    lista_desordenada = []
    for x in range(10):
        lista_desordenada.append(x)
    lista_desordenada = [5,4,3,2,1]
    lista_ordenada = bubble_sort(lista_desordenada)
    print(lista_ordenada)