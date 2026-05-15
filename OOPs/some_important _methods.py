#NORMAL INSTANCE METHODS

#normal methods in oop where class ,object and constructor are used

class Student:

    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello", self.name)

s1 = Student("Aravind")

s1.greet()



#CLASS METHODS

#Class methods work with class itself instead of object