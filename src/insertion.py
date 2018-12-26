def insertionSort(l):
    for i in range(1,len(l)):
        j = i
        sorting = l[j]
        while sorting < l[j-1] and j > 0:
            l[j] = l[j-1]
            j -= 1
        l[j] = sorting
