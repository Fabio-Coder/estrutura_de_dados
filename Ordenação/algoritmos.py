from Analise_de_complexidade.cronometro import cronometro_ns, cronometro
from Ordenação.bogosort import bogosort
from Ordenação.quick_sort import quick_sort
from Ordenação.selection_sort import selection_sort
from Ordenação.bubble_sort import bubble_sort


def chama_algoritmo(algoritmo, max_elementos, str_algoritmo):
    print(f'Lista de tempos para o algoritmo {algoritmo}:')
    print('=================================================')
    for i in range(0, max_elementos, 100):
        lista_desordenada = []
        elementos = i
        for x in range(elementos, 0, -1):
            lista_desordenada.append(x)
        inicio = cronometro()
        inicio_ns = cronometro_ns()
        lista_ordenada = algoritmo(lista_desordenada)
        fim = cronometro()
        tempo_s = fim - inicio
        fim_ns = cronometro_ns()
        print(f'{str_algoritmo}: Tempo (s) para {elementos} elementos: %2f{tempo_s}')
        # print(f'{algoritmo}: Tempo (ns) para {elementos} elementos: {fim_ns - inicio_ns}')
        print('=================================================')


if __name__ == '__main__':
    chama_algoritmo(bubble_sort, 1000, 'Bubble Sort')
    chama_algoritmo(selection_sort, 10000, 'Selection Sort')
    chama_algoritmo(merge_sort, 1000, 'Merge Sort')
    chama_algoritmo(insertion_sort, 1000, 'Insertion Sort')
    chama_algoritmo(bogosort, 10, 'Estou com Sorte')
