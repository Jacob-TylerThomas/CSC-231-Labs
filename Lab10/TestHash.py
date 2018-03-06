from Hashtable import *
import random, time

def randomString(n):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    string=""
    something=random.randint(4, n)
    for i in range(something):
        r=random.randint(0, 25)
        character=alphabet[r]
        string += character

    return string

n=10
print('N, \t SumHash,\t SumDict')
for n in range(100, 3001, 100):
    myTable=HashTable()
    myDict={}
    sumHash=0
    sumDict=0
    for i in range(n):
        key=randomString(10)
        start = time.clock()
        myTable[key]=key
        end = time.clock()
        sumHash += end-start

        start2 = time.clock()
        myDict[key]=key
        end2 = time.clock()
        sumDict += end2-start2


    print(n,"\t",sumHash,"\t",sumDict)

