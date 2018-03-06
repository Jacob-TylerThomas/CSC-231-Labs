def controlRecursion(n):
    if n > 0:
        print("This is a recursive method")
        controlRecursion(n - 1)
controlRecursion(5)
