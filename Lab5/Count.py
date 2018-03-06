def count(s, ch):
    if len(s)==0:
        return 0
    if s[0]==ch:
        return 1 + count(s[1:], ch)
    else:
        return 0 + count(s[1:], ch)
s=input("give me a string: ")
c=input("give me a character: ")
print(c, "occurs", count(s,c), "times in", s)
