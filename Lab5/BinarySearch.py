def binSearch(list, target):
    return binSearchHelper(list, target, 0, len(list) - 1)
def binSearchHelper(list, target, left, right):
    if left > right:
        return False
    middle = (left + right)//2
    if list[middle] == target:
        return True
    elif list[middle] > target:
        return binSearchHelper(list, target, left, middle - 1)
    else:
        return binSearchHelper(list, target, middle + 1, right)
list = [5, 10, 15, 20, 25, 33, 50, 75, 90]
answer = binSearch(list, 25)
if answer:
    print("25 is in the list")
else:
    print("25 is not in the list")
answer = binSearch(list, 90)
if answer:
    print("90 is in the list")
else:
    print("90 is not in the list")
answer = binSearch(list, 40)
if answer:
    print("40 is in the list")
else:
    print("40 is not in the list")