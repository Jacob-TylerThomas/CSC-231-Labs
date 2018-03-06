import math
# list = ['a', 'b']
# while True:
#     try:
#         list.pop()
#     except:
#         print("Done")
#         break

print("I will compute the square root")
number = input("Enter a number: ")
try:
    num = float(number)
    if num < 0:
        raise RuntimeError("You can’t use a negative number")
    print(math.sqrt(num))

except ValueError:
    print("That is not a number!")

except RuntimeError as e:
    print(e)