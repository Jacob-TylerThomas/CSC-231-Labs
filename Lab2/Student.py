class Student:
    def __init__(self, first, last, gpa):
        self.firstName=first
        self.lastName=last
        self.gpa=gpa
    def __str__(self):
        return self.firstName + " " + self.lastName + "\t" + "GPA: " + str(self.gpa)
    def setGPA(self, g):
        self.gpa=g



