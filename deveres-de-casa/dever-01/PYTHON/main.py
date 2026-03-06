import random
import time

TAMANHOS = [1000, 2000, 10000, 20000, 50000]


def insertion_sort(lista): 

    for i in range(1, len(lista)):
        aux = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > aux: 
            lista[j+1] = lista[j]
            j-=1
        lista[j+1] = aux

for n in TAMANHOS: 
    lista = [random.randint(0,42) for _ in range(n)]

    lista_insert = lista.copy()
    lista_sort = lista.copy()

    """
    INSERTION
    """

    inicio_insert = time.time()
    insertion_sort(lista_insert)
    fim_insert = time.time()

    tempo_insert = fim_insert - inicio_insert

    """
    SORT
    """

    inicio_sort = time.time()
    lista_sort.sort()
    fim_sort = time.time()

    tempo_sort = fim_sort - inicio_sort

    print(f"\nn = {n}")
    print("Insertion sort: ", tempo_insert)
    print("Python sort: ", tempo_sort)

