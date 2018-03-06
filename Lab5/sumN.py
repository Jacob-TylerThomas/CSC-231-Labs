def sumN(n):
    if n==0:
        return 0
    return n + sumN(n-1)
user_input=input("Enter a number: ")
num=int(user_input)
print("The sum from 0 to", num, "is", sumN(num))
print("The answer should be:", num*(num+1)/2)