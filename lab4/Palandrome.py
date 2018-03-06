from Deque import *

def isPalindrome(s):
    deck = Deque()
    for character in s:
        deck.addFront(character)
    while deck.size() > 1:
        if deck.removeFront()!=deck.removeRear():
            return False
    return True
user_input=input("Give ma a string to test: ")

if isPalindrome (user_input):
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")
