from Stack import *


user_input=input('Enter an integer: ')
number=int(user_input)
stack=Stack()

while number !=0:
    remainder=number % 2
    stack.push(remainder)
    number= number//2 #big O is logn

while not stack.isEmpty():
    print(stack.pop(), end="")
