from Stack import *

user_string=input("Enter a string: ")
stack=Stack()
everythingOK=True
for character in user_string:
    if character== '(':
        stack.push(character)
    elif character == ')':
        if stack.isEmpty():
            print("Too many right parentheses")
            everythingOK=False
            break
        else:
            stack.pop()
if everythingOK:
    if stack.isEmpty():
        print('The parentheses are balanced.')

    else:
        print("Too many left parentheses.")

