from timeit import default_timer as timer
from src import insertion
res = []

with open(r'src_tests\ordered.dat', 'r') as file:
    for line in file:
        arr1 = [int(x) for x in line.rstrip().split(' ')]
        s = timer()
        insertion.insertionSort(arr1)
        e = timer()
        res.append('Insertion ' + str(len(arr1)) + ' ' + str(e-s) + ' seconds\n')
file.close()

with open(r'res.dat', 'a') as file:
    file.write('\nOrdered elements from 0 to N\n')
    for i in res:
        file.write(i)
