from bubbleSort import *
from insertionSort import *
from selectionSort import *
import random, time

n=100
print('N\tBComp\tBSwaps\tIComps\tISwaps\tSComps\tSSwaps')
for n in range (100, 3000, 100):
    myList = []
    for i in range (n):
        myList.append(random.randint(0, 2*n))

    myList2=list(myList)
    myList3=list(myList)


    start=time.clock()
    bubbleComparisons, bubbleSwaps=bubbleSort(myList)
    end=time.clock()

    # start2 = time.clock()
    # bubbleSort2(myList2)
    # end2 = time.clock()

    start2 = time.clock()
    insertComparisons, insertSwaps=insertionSort(myList2)
    end2 = time.clock()

    start3 = time.clock()
    selectionComparisons, selectionSwaps=selectionSort(myList3)
    end3 = time.clock()

    print(n, '\t', bubbleComparisons, '\t',bubbleSwaps, '\t', insertComparisons, '\t', insertSwaps, '\t', selectionComparisons,
          '\t', selectionSwaps)