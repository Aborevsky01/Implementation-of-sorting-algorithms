from timeit import default_timer as timer
from src import quick
res = []

with open(r'src_tests\orderedSeq.dat', 'r') as file:
    for line in file:
        arr1 = [int(x) for x in line.rstrip().split(' ')]
        s = timer()
        quick.quickSort(arr1)
        e = timer()
        res.append('Quick ' + str(len(arr1)) + ' ' + str(e-s) + ' seconds\n')
file.close()

with open(r'res.dat', 'a') as file:
    file.write('Ordered elements from 0 to N\n')
    for i in res:
        file.write(i)
