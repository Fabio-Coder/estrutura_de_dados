from Analise_de_complexidade.cronometro import cronometro_ns, cronometro
from Ordenação.quick_sort import quick_sort, divisao, quick_sort_auxiliar
from Ordenação.selection_sort import selection_sort
from Ordenação.bubble_sort import bubble_sort

algoritmo = 'quick sort'
print(f'Lista de tempos para o algoritmo {algoritmo}:')
print('=================================================')
for i in range(0,1001,100):
    lista_desordenada = []
    elementos = i
    for x in range(elementos, 0, -1):
        lista_desordenada.append(x)
    inicio = cronometro()
    inicio_ns = cronometro_ns()
    lista_ordenada = quick_sort(lista_desordenada)
    fim = cronometro()
    fim_ns = cronometro_ns()
    print(f'Tempo de execução (s) para {elementos} elementos: {fim - inicio}')
    print(f'Tempo de execução (ns) para {elementos} elementos: {fim_ns - inicio_ns}')
    print('=================================================')

algoritmo = 'bubble_sort'
print(f'Lista de tempos para o algoritmo {algoritmo}:')
print('=================================================')
for i in range(0,1000,100):
    lista_desordenada = []
    elementos = i
    for x in range(elementos, 0, -1):
        lista_desordenada.append(x)
    inicio = cronometro()
    inicio_ns = cronometro_ns()
    lista_ordenada = bubble_sort(lista_desordenada)
    fim = cronometro()
    fim_ns = cronometro_ns()
    print(f'Tempo de execução (s) para {elementos} elementos: {fim - inicio}')
    print(f'Tempo de execução (ns) para {elementos} elementos: {fim_ns - inicio_ns}')
    print('=================================================')

algoritmo = 'selection sort'
print(f'Lista de tempos para o algoritmo {algoritmo}:')
print('=================================================')
for i in range(0,10001,1000):
    lista_desordenada = []
    elementos = i
    for x in range(elementos, 0, -1):
        lista_desordenada.append(x)
    inicio = cronometro()
    inicio_ns = cronometro_ns()
    lista_ordenada = selection_sort(lista_desordenada)
    fim = cronometro()
    fim_ns = cronometro_ns()
    print(f'Tempo de execução (s) para {elementos} elementos: {fim - inicio}')
    print(f'Tempo de execução (ns) para {elementos} elementos: {fim_ns - inicio_ns}')
    print('=================================================')