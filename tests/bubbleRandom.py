from timeit import default_timer as timer
from src import bubble
res = []

with open(r'src_tests\random.dat', 'r') as file:
    for line in file:
        arr1 = [int(x) for x in line.rstrip().split(' ')]
        s = timer()
        bubble.bubbleSort(arr1)
        e = timer()
        res.append('Bubble ' + str(len(arr1)) + ' ' + str(e-s) + ' seconds\n')
file.close()

with open(r'res.dat', 'a') as file:
    file.write('\nRandom elements from 0 to N\n')
    for i in res:
        file.write(i)
