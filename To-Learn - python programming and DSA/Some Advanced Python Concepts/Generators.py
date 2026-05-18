#GENERATORS

#generators are used for lazy computation Meaning produce values only when needed
# instead of storing everything in memory


#suppose when a list is created with huge number of values
nums = [x for x in range(100000000)]

#this creates 100 million numbers in memory
#huge memory needed very inefficient


#generate values one-by-one

#What If We Only Need One Value at a Time?

#Instead of storing ALL values:
#generate values one-by-one
#This is exactly what generators do

#it is a special iterator that produces values lazily

#Generator does NOT create all values immediately
#Instead creates values one at a time only when requested

#creating a generator

#generators use  yield  rather than  return


num = [1,2,3,4,5]

def counter():

    yield 1
    yield 2
    yield 3

g = counter()

print(g)

print(next(g))
print(next(g))


#generator function returns generator object NOT actual values immediately.

#yield 1 → pause
#yield 2 → pause
#yield 3 → pause'

#generator version off 1 million nums

numS = (x*x for x in range(1000000))   #() used for generator like [] for list comprehension

print(next(numS))

for num in numS:
    print(num)


#Infinite Generators

def fib():
    a, b = 0, 1
    while True:

        yield a
        a, b = b, a + b

g = fib()

for _ in range(5):

    print(next(g))

#INFINITE NUMBERS WITH OUT INFINITE MEMORY
#because generator take current state not entire sequence



#Generator State Preservation

def test():

    print("A")

    yield 1

    print("B")

    yield 2

g = test()

next(g)

#output
#A
#1

next(g)

#output
#B
#2

#Resumes EXACTLY where paused


# send()

#send() is used for receiving data in a generator

def calculator():

    while True:

        x = yield

        print(x * 2)

g = calculator()

next(g)

g.send(10)
g.send(20)

# Normal Function	  Generator
# returns once	      yields many times
# return	              yield
# no pause	          pauses/resumes
# stores everything    lazy generation

