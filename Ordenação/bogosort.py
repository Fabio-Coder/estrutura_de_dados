from random import shuffle


def bogosort(lista):
    sentinela = False
    cont = 0
    while not sentinela:
        sentinela = True
        for i in range(len(lista)-1):
            if lista[i] > lista[i + 1]:
                sentinela = False
        if sentinela == False:
            shuffle(lista)
            cont += 1
            print(cont)
        else:
            print(f'Fui ordenado em apenas {cont} iteracoes!')
            print(lista[:])


if __name__ == '__main__':
    lista = [5, 4, 3, 2, 1]
    bogosort(lista)
