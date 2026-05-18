#iterators

#Iterator is an object that:
#returns values one-by-one
#instead of giving everything at once.


nums = [10,20,30]

it = iter(nums)

print(it)

print(next(it)) #getting values
print(next(it))

#[10,20,30]
#↑ current position
#after first next it moves forward to 20

#after all values
#python stops iteration


#Python loops internally use iterators

#eg
num = [1,2,3]

for num in nums:
    print(num)

#internally
it = iter(nums)

while True:

    try:
        num = next(it)

        print(num)

    except StopIteration:
        break

#iterable and iterator

#iterables are object when can loop over
#eg : lists,dictionary,files,tuple,set etc

#iterator are objects used to process value one by one using next()

#Iterable → creates iterator

#list is not a iterator
#why
nums = [1,2,3]

next(nums) #----> error

#because lists can implement  __next__()  directly thats whys  an iterator is needed here

it = iter(nums)

print(next(it))

#an iterator protocol
#return __iter__() the iterator ----> iter()
#return __next__() the next value  -----> next()

#creating a custom iterator
class Count:

    def __init__(self, max_value):

        self.current = 1
        self.max_value = max_value

    def __iter__(self):

        return self

    def __next__(self):

        if self.current > self.max_value:
            raise StopIteration

        value = self.current

        self.current += 1

        return value

counter = Count(5)

for num in counter:
    print(num)


#Iterators allow lazy evaluation Meaning values produced only when needed

#Generators Are Iterators
#it automatically implements iterator protocol

#Iterator vs        Generator
#manual __next__	uses yield
#more code	        easier
#flexible	        concise
#custom behavior	automatic state handling