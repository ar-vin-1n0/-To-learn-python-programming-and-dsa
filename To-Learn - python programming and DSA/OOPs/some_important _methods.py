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

#A class method is a method that works with the CLASS ITSELF instead of individual objects

#@classmethod - decorator used for class method

class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):
        print(cls.school)


Student.show_school()

#output  -  ABC School

#cls  similar to self

#Student.show_school(Student)  internal reality cls - becomes - student

#sometimes functionality belongs to whole class NOT individual objects

#school = "ABC School" --- is a class variable

#alternative constructor
class StudentA:

    def __init__(self, name):
        self.name = name

    @classmethod
    def from_string(cls, data):

        name = data.split("-")[0]

        return cls(name)

s1 = StudentA.from_string("Aravind-21")

print(s1.name)



#STATIC METHODS

#normal functions inside class namespace

#static methods dont have self or cls

# @staticmethod

class MathUtils:

    @staticmethod
    def add(a, b):
        return a + b

print(MathUtils.add(2,3))

#static methods doesnt know or care about object state and class state it is independent




#MAGIC METHODS / DUNDER METHODS

#Magic methods are one of Python’s MOST powerful features.They allow custom objects to behave like:

#numbers
#strings
#lists
#dictionaries
#iterators
#functions

#they are special methods automatically called by Python in special situations

#they are represented using __double_underscores__

#You usually do NOT call magic methods directlyPython calls them automatically.

#print(obj)   --- when called python internally calls obj.__str__()


#1. __init__ — Constructor is also a magic method

#2. __str__ --> controls behavior
  #without __str__

class Student:

    def __init__(self, name):
        self.name = name

s1 = Student("Aravind")

print(s1) # ----->   <__main__.Student object at 0x000001>  really ugly addressing

#with __str__

class StudentA:

    def __init__(self, name):
        self.name = name

    def __str__(self):

        return f"Student: {self.name}"

s2 = StudentA("Aravind")

print(s2)  # ------>  print(s1.__str__())  ------->Student: Aravind


#3 __len__

#controls behavior
class Team:

    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

t = Team(["a", "b", "c"])

print(len(t))  #-------> t.__len__()

#objects now behave like built-in containers


#4 __add__ , __sub__,__mul__ --> operator methods

#controls + operator

#eg
class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):

        return self.value + other.value

a = Number(10)
b = Number(20)

print(a + b)  #----> a.__add__(b)


#5 __eq__

#controls == behavior


class StudentB:

    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):

        return self.marks == other.marks

s1 = Student(90)
s2 = Student(90)

print(s1 == s2) # --->> true ------> s1.__eq__(s2)


#6 __repr__ — Developer Representation

#used for repr(obj) and debugging  ---- used by devs

class StudentC:

    def __repr__(self):
        return "Student Object"

#diff btw __str__ & __repr__
class Student:

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Name: {self.name}"

    def __repr__(self):
        return f"Student('{self.name}')"


s = Student("Aravind")

print(str(s))    #---->Name: Aravind

print(repr(s))   # ---->Student('Aravind')



#7 __getitem__

#controls index behavior of an object

class MyList:

    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

m = MyList([10,20,30])

print(m[1])  #------> m.__getitem__(1)



#8 __call__

#Makes object callable like function

class Greeter:

    def __call__(self):
        print("Hello")

g = Greeter()

g() #----> g.__call__()


#9 __setitem__

class Numbers:

    def __init__(self):
        self.data = {}

    def __setitem__(self, key, value):

        self.data[key] = value

n = Numbers()

n[0]="zero"

#10 __contains__

#used to check a membership like is

class Numbers:

    def __init__(self):
        self.values = [1,2,3]

    def __contains__(self, item):

        return item in self.values

n = Numbers()

print(2 in n)

