def insertionSort(alist):
    countComparisons=0
    countSwaps=0
    for index in range(1,len(alist)):

        currentvalue = alist[index]
        position = index

        countComparisons +=1
        while position>0 and alist[position-1]>currentvalue:
            countComparisons+=1
            countSwaps+=1
            alist[position]=alist[position-1]
            position = position-1

        alist[position]=currentvalue
    return countComparisons, countSwaps