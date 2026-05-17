#MATH MODULE

#math module provides math functions

import math

#SRQT
#finds square root off a number
print(math.sqrt(25))

#pow
#finds power of a number x by a number y
print(math.pow(10,5))

#ceil
#rounds up a number
print(math.ceil(9.3))

#floor
#rounds down a number
print(math.floor(9.9))


#CONSTANTS

#pi
print(math.pi) #give pi value of 3.14

#e
print(math.e) #gives euler number

#factorial
print(math.factorial(5)) #give factorial values

#trignometry

print(math.sin(50)) #give sin value
#ETC

#logarithms
print(math.log(10))



#COLLECTION MODULE

#collection module is used like a container for data structures like list,tuples,dictionary etc but beyond them

from collections import Counter, defaultdict, deque

#Counter

#used for frequency counting

nums = [1,1,2,3,3,3]

count = Counter(nums)

print(count)

print(count[3]) #accessing frequencies

     #most_common method in counter

print(count.most_common(1)) # finds elements with most frequency

#time complexity of counter = O(n)



#Defaultdict

#unlike dictionary defaultdict creates default value in a empty dictionary

#eg
d = defaultdict(int) # int , lists, set are used here

d["a"] += 1

print(d) #normal dict wont print anything and show error

#grouping
groups = defaultdict(list)

groups["python"].append("Aravind")

print(groups)


#DEQUE

#deque is kind off a double ended queue

#lists is lower to access element from front/left
#while deque is faster in both ends left and right

#time complexity for every operation in deque is O(1)
from collections import deque

d = deque([1,2,3])

d.append(4) #appends to right
d.appendleft(0) #appends to letf

print(d)

d.pop() #removes element from right
d.popleft() #removes element from left
print(d)

#follows fifo rule - first in first out


#NAMED TUPLE

#adds meaning to tuple fields
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])

p = Point(3,4)

print(p.x)






