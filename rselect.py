#Si eligieramos el pivote como la media del array, entonces tendríamos asegurado que el array se dividiría a la mitad.
#Por lo tanto, T <= 2(n/2) + O(n) = O(nlogn)
#Sin embargo, al elegir un pivote random, el número seleccionado muy probablemente estará entre 25% y 75%.
#Por lo tanto, en promedio el algoritmo corre en O(nlogn), siendo el peor caso O(n^2)

from random import randint
from random import seed
from datetime import datetime

def rselect(array, i, l, r):
    if(len(array[l:r + 1]) == 1):
        #print("si" + str(array[l]))
        return array[l]
        
    index = randint(l, r - 1) #Get index pivot
    j = partition(array, index, l, r) #Get the pivot poistion once partitionated
    print(i, j, array[l:r], array, l, r)
    if(j-l == i):
        #print(array[j])
        return array[j]
    #print(array)
    elif(i < j-l):
        return rselect(array, i, l, j)
    else:
        return rselect(array, i - (j + 1), j + 1, r)


def partition(array, index, l, r):
    pivot = array[index]
    swap(array, l, index)
    print(index, pivot)
    i = l + 1

    for j in range(l + 1, r):
        if(array[j] < pivot):
            swap(array, i, j)
            i += 1

    swap(array, l, i - 1)
    return (i - 1)

def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

seed(datetime.now())
array = [12, 52, 3, 23, 10, 5, 63, 100, 232, 1, 0, 55]
print(array)

print(rselect(array, 3, 0, len(array)))
#print(array)
