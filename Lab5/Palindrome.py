def isPalindrome(s):
    if len(s)==0:
        return True
    if len(s)==1:
        return True
    if s[0] != s[-1]:
        return False
    return isPalindrome(s[1:-1])
x = input("Give me a string: ")
if isPalindrome(x):
    print("Yes,", x, "is a palindrome.")
else:
    print("No,", x, "is NOT a palindrome.")
