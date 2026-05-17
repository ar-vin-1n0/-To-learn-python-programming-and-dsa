#LAMBDA

#Lambda is anonymous small function
#functions without normal name

#syntax
# lambda arguments: expression

#normal functions
def square(x):

    return x * x


#lambda version

squareA = lambda x : x * x

#lambda returns function object
#its exist for small temporary functions especially when function used only once

#eg -- sorting
students = [
    ("Aravind", 21),
    ("John", 19),
    ("Alex", 25)
]

students.sort(
    key=lambda student: student[1]
)

print(students)


#lambda with conditions

check = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check(4))


#lambda with map()

nums = [1,2,3,4]

result = map(
    lambda x: x * x,
    nums
)

print(list(result))

#here expression /lambda is Applied  to every element


#Lambda with filter()

numsA = [1,2,3,4,5,6]

resultA = filter(
    lambda x: x % 2 == 0,
    nums
)

print(list(resultA))

#filter() keeps elements where condition is True


#Lambda with sorted()

words = ["apple", "kiwi", "banana"]

resultB = sorted(
    words,
    key=lambda word: len(word)
)

print(resultB)

#Sort based on length