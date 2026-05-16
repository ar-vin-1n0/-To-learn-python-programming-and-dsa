#decorators

#Decorator is a function that takes another function adds extra behavior returns modified function
#its is used to add an extra layer to an existing function

#Original function
#        ↓
#Decorator wraps it
#        ↓
#Enhanced function


def logger(func):               #this is the decorator function

    def wrapper():

        print("Function started")

        func()

        print("Function ended")

    return wrapper

@logger          #this is a decorator being called in this function
def task():
    print("Working")


#Function started
#Working
#Function ended


#decorator if functions have arguments

#Normal wrapper fails when function has arguments
#*args
#**kwargs
#are the solutions for this

def decorator(func):

    def wrapper(*args, **kwargs):

        print("Before")

        func(*args, **kwargs)

        print("After")

    return wrapper


@decorator
def greet(name):

    print(name)

print(greet("aravind"))


#decorators in OOP

#these are built in decorator used in oop
#modifies behavior of function or methodWITHOUT changing original function code directly


# @classmethod

#normal instance class

class Student:

    def greet(self):
        print("hello")

s1 = Student()

s1.greet()   #----->  Student.greet(s1)


#Sometimes method should work with class itself not object That’s where @classmethod comes.

#Eg
class Student:

    school = "ABC School"

    @classmethod
    def show_school(cls):

        print(cls.school)

Student.show_school()  #----->  Student.show_school(Student)


# @staticmethod

#do not receive self or cls They behave like normal functions inside class

class MathUtils:

    @staticmethod
    def add(a, b):

        return a + b


print(MathUtils.add(1, 2))

#logically belongs to class but doesn’t need object/class data


# @property

#without property

class StudentA:

    def __init__(self, marks):
        self.marks = marks

sa = StudentA(10)
print(sa.marks)

#rules
#marks cannot be negative
#marks cannot exceed 100
#here without property code breaks

#with property

class StudentB:

    def __init__(self, marks):
        self.__marks = marks

    def get_marks(self):

        return self.__marks

s3 = StudentB(10)
print(s3.get_marks())

class StudentC:

    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):

        return self.__marks

s4 = StudentC(10)
print(s4.marks)


class StudentD:

    def __init__(self, marks):
        self.__marks = marks

    @property
    def marks(self):

        return self.__marks

    @marks.setter
    def marks(self, value):

        if value < 0:
            raise ValueError("Marks cannot be negative")

        self.__marks = value

s5 = StudentD(90)

s5.marks = 95


#@abstractmethod

#used in abstraction
from abc import ABC, abstractmethod

#Abstract Classes Abstract class incomplete blueprint Cannot create objects directly

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class DogD(Animal):   #--> this causes error  because dog failed to implement abstractmethod of sound()
    pass


class DogA(Animal):

    def sound(self):

        print("Bark")

d = DogA()

d.sound()