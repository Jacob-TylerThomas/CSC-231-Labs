import random
import time
def find(list, x):
    for a in list:
        if a==x:
            return True
    return False
n=100
for n in range(50000, 1000001, 50000):
    sum=0
    for experiment in range(0, 10):
        numbers=[]
        for i in range(0, n):
            ran=random.randrange(0, 2*n +1)
            numbers.append(ran)

        # print(numbers)
        # print(find(numbers, 5))
        # print(find(numbers, 150))
        # print(find(numbers, 101))

        # generate random number not in list
        ran=random.randrange(0, 2*n +1 )
        while ran in numbers:
            ran = random.randrange(0, 2 * n + 1)

        # print(ran, "is not in the list")
        # print(numbers)

        start=time.clock()
        result=find(numbers, ran)
        end=time.clock()
        sum += (end -  start)
    print(n, "\t", sum/10)

