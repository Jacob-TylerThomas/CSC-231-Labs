from Hashtable import *

myTable=HashTable()
myTable.put(200, "dog",)
value=myTable.get(200)
print("value is", value)
myTable.put(77, 22.5)
value=myTable.get(77)
print('value is', value)
myTable["duck"]="eider"
print(myTable["duck"])
print("length is", len(myTable))

user_input=int(input("Give me a number: "))
print(user_input, myTable.isPrime(user_input))
