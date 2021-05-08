def quick_sort(lista):
    quick_sort_auxiliar(lista, 0, len(lista) - 1)


def quick_sort_auxiliar(lista, primeiro, ultimo):
    if primeiro < ultimo:
        ponto_de_ruptura = divisao(lista, primeiro, ultimo)
        quick_sort_auxiliar(lista, primeiro, ponto_de_ruptura - 1)
        quick_sort_auxiliar(lista, ponto_de_ruptura + 1, ultimo)


def divisao(lista, primeiro, ultimo):
    pivo = lista[primeiro]
    esquerda = primeiro + 1
    direita = ultimo
    sentinela = False

    while not sentinela:
        while esquerda <= direita and lista[esquerda] <= pivo:
            esquerda += 1

        while direita >= esquerda and lista[direita] >= pivo:
            direita -= 1

        if direita < esquerda:
            sentinela = True
        else:
            lista[esquerda], lista[direita] = lista[direita], lista[esquerda]

    lista[primeiro], lista[direita] = lista[direita], lista[primeiro]

    return direita


if __name__ == '__main__':
    lista_exemplo = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    quick_sort(lista_exemplo)
    print(lista_exemplo)

    # lista_desordenada = []
    # elementos = 990
    #for x in range(elementos, 0, -1):
        #lista_desordenada.append(x)
    #lista_ordenada = quick_sort(lista_desordenada)
