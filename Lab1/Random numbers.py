import random

file_name=open("numbers.txt", "w")
howMany=random.randrange(500, 1001)

for i in range(0, howMany):
    numbers=random.randrange(-100, 101)
    file_name.write("%d\n" % numbers)


file_name.close
