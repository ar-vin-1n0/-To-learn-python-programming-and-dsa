#List comprehensions

#List comprehension is compact way to create lists
#using:
#loops
#conditions
#expressions

#eg - syntax
#  [expression for item in iterable]

#expression	-   value to store
#item	    -   current element
#iterable	-   list/range/string/etc

#traditionally

nums = [1,2,3,4,5]


resultT = []

for num in nums:

    resultT.append(num * num)

print(resultT)

#After List comprehension               #num * nums  -----> is the expression
                                        #for num in nums  -----> the loop with num as the item and nums as the iterable
result = [num * num for num in nums]

print(result)

#reduced lines off code without changing the process


#another eg
names = ["aravind", "john"]

resultA = []

for name in names:

    resultA.append(name.upper())

print(resultA)

#After List comprehension

resultB = [name.upper() for name in names]

print(resultB)


#List Comprehension with Conditions


#eg - syntax
#[expression for item in iterable if condition]

nums = [1,2,3,4,5,6]

evens = [num for num in nums if num % 2 == 0]   #if num % 2 == 0 ----> is the condition

print(evens)


#eg another example
words = ["cat", "elephant", "dog", "tiger"]

resultD = [
    word
    for word in words
    if len(word) > 4
]

print(resultD)


#Conditional Expression Inside Comprehension

#syntax
# [
#       value_if_true
#       if condition
#       else value_if_false
#       for item in iterable
#  ]

#eg


resultE = [
    "even"
    if num % 2 == 0
    else "odd"
    for num in nums
]

print(resultE)


#Nested List Comprehensions

#eg  -  matrix flattening
matrix = [
    [1,2],
    [3,4],
    [5,6]
]

resultF = [
    num
    for row in matrix
    for num in row
]

print(resultF)


#SET COMPREHENSIONS

nums = [1,1,2,3]

resultg = {
    num
    for num in nums
}

print(resultg)

#DICTIONARY COMPREHENSIONS

squares = {
    num: num * num
    for num in nums
}

print(squares)


#List comprehensions are usually faster than manual loops because Python internally optimizes them