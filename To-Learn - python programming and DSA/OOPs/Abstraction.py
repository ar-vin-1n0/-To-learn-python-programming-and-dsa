#Abstraction

#hide internal complexity
#show only essential features

#Good software hides complexity behind
#clean interfaces is achieved using abstraction

#eg
class CoffeeMachine:

    def make_coffee(self):

        self.__boil_water()
        self.__add_coffee()
        self.__pour()

#user only uses
#c=CoffeeMachine()
#c.make_coffee()

#internal complexities are hidden
#Abstraction make large systems possible


#Abstract classes

#abstract classes act as incomplete blueprint/template
#it defines what subclasses MUST have
#its say rules that Any child class MUST implement these methods

from abc import ABC, abstractmethod #abc --> Abstract base class

class Animal(ABC):             #means Animal is abstract class means it is an incomplete class

    @abstractmethod            #means child classes MUST implement this method
    def sound(self):           #Parent only declares method. No real implementation.
        pass

#a = Animal() is invalid
#Animal is incomplete
# python  doesnt know what to make of animal class cuz its empty so object creation is blocked

class Dog(Animal):

    def sound(self):     #child class must complete the abstract method
        print("Bark")

#Abstract class provides common interface ,all animal classes GUARANTEED to have sound()

#without abstract class if one forgets to create a sound method in dog
#and when
d= Dog()
d.sound() #if sound method isnt in class dog then it crashes

#Abstract Classes Prevent This ,Python forces subclasses to implement required methods

