from shellSort import *
import random, time

n=100
experiment=10
for n in range(100, 20600, 1000):
    sum=0
    sum2=0
    sum3=0
    for experiments in range(experiment):
        myList=[]
        for i in range(n):
            myList.append(random.randint(0, 2*n))

        myList2=list(myList)
        myList3=list(myList)

        start=time.clock()
        shellSort(myList)
        end=time.clock()
        sum += end-start

        start = time.clock()
        shellSortShell(myList2)
        end = time.clock()
        sum2 += end - start

        start = time.clock()
        shellSortHibbard(myList3)
        end = time.clock()
        sum3 += end - start

    print(n, '\t', sum/experiment, '\t', sum2/experiment, '\t', sum3/experiment)
