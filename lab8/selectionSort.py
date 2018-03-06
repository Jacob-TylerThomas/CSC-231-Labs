def selectionSort(alist):
    countComparisons=0
    countSwaps=0
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax=0
        for location in range(1,fillslot+1):
            countComparisons+=1
            if alist[location]>alist[positionOfMax]:
                positionOfMax = location

        countSwaps+=1
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp

    return countComparisons, countSwaps
