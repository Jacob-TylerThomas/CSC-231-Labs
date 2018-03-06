def bubbleSort(alist):
    countComparisons=0
    countSwaps=0
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            countComparisons += 1
            if alist[i]>alist[i+1]:
                countSwaps += 1
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

    return countComparisons, countSwaps


# def bubbleSort2(alist):
#     for passnum in range(len(alist)-1,0,-1):
#         for i in range(passnum):
#             if alist[i]>alist[i+1]:
#                 alist[i], alist[i+1]=alist[i+1], alist[i]