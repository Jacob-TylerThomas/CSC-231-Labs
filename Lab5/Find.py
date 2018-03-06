def find(alist, element):
    if len(alist)==0:
        return False
    if alist[0] == element:
        return True
    return find(alist[1:], element)
a = [1, 17, 99, -4, 3]
print(find(a, 3))
print(find(a, 5))
print(find(a, 99))
