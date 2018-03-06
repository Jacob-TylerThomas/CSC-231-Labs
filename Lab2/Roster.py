from Student import *
inputfile=open("accounts.txt","r")
students=[]
for line in inputfile:
    tokens=line.split()
    last=tokens[0]
    first=tokens[1]
    gpa=float(tokens[2])
    stu=Student(first, last, gpa)
    students.append(stu)
for s in students:
    print(s)
maxStudent=students[0]
for s in students:
    if s.gpa<maxStudent.gpa:
        maxStudent=s
print("The student with the highest gpa is: ", maxStudent)
inputfile.close