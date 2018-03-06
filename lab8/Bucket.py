import random, time
from mergeSort import *

n=100
for n in range(100000, 300000, 25000):
    myList=[]
    for i in range(n):
        myList.append(random.randint(0, 100))
    myList2=list(myList)
    start=time.clock()
    buckets=101*[0]
    for number in myList:
        buckets[number]+=1

    sortedList=[]

    for index in range(len(buckets)):
        for count in range(buckets[index]):
            sortedList.append(index)

    end=time.clock()


    start2=time.clock()
    mergeSort(myList2)
    end2=time.clock()

    print(n, '\t', end-start, '\t', end2-start2)


# print(myList)
# print(sortedList)