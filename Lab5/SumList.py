def sumList(list):
    if len(list) == 0:
        return 0
    else:
        return list[0] + sumList(list[1:])
#big O equal order n
print(sumList([1,2,3,4]))
