def quickSort(l):
    if len(l) <= 1:
        return l
    pivot = l[len(l)//2]
    first = l[0]
    last = l[len(l)-1]
    if pivot < first < last or pivot > first > last:
        pivot = first
    elif pivot < last < first or pivot > last > first:
        pivot = last
    less = []
    more = []
    countPivot = 0
    for i in l:
        if i < pivot:
            less.append(i)		
        elif i > pivot: 
            more.append(i)
        else:
            countPivot += 1
    less = quickSort(less)
    more = quickSort(more)
    return less + [pivot]*countPivot + more

