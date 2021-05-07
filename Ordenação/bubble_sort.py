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

if __name__ == '__main__':
    lista_desordenada = []
    elementos = 10000
    for x in range(elementos,0,-1):
        lista_desordenada.append(x)
    inicio = cronometro()
    inicio_ns = cronometro_ns()
    lista_ordenada = bubble_sort(lista_desordenada)
    fim = cronometro()
    fim_ns = cronometro_ns()
    print(f'Tempo de execução (s) para {elementos} elementos: {fim-inicio}')
    print(f'Tempo de execução (ns) para {elementos} elementos: {fim_ns - inicio_ns}')
