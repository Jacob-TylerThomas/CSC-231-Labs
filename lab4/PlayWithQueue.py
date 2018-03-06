from Queue import *

myQ= Queue()
myQ.enqueue("dog")
myQ.enqueue("cat")
myQ.enqueue("elephant")
x=myQ.dequeue()
print(x)
while not myQ.isEmpty():
    print(myQ.dequeue(), end=" ")


