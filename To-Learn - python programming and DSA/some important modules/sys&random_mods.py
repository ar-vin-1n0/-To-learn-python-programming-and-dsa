#SYS MODULE

#sys module helps to interact with interpreter,runtime env,command line execution ,system level behavior

import sys

#sys.argv - argument vector
#it store command-line arguments for python script

#num1 = int(sys.argv[1]) #these arguments can only be assigned from command line
#num2 = int(sys.argv[2])

#print(num1 + num2)

#in command-line
#python filename.py 10,20
#output = 30

#sys.exit()

#exit() Stops program immediately

#age = -1

#if age < 0:
    #sys.exit("Invalid age")

#print("Valid")

#exit() can be used for fatal errors
#stopping scripts safely

#sys.version - shows python version


#sys.path()
#show directories where python searches for modules


def random_mod():
    #RANDOM MODULE

    #The random module is Python’s built-in module for generating pseudo-random values

    import random

    #random.randint()
    #creates randoms integers in a range

    #eg
    print(random.randint(1, 10))


    #random.random()

    #create a random float from 0 - 1

    print(random.random())


    #random.choice()
    #pick a random from a sequence of elements -list,tuples,string

    #eg
    names = ["Aravind", "John", "Alex"]

    print(random.choice(names))


    #random.shuffle()
    #randomly shuffles and rearranges lists

    nums = [1,2,3,4,5]

    random.shuffle(nums)

    print(nums)


    #random.sample()
    #creates random subsets from a list

    #eg
    result = random.sample(nums, 2)

    print(result)


    #random.seed()
    #seed is a starting point where system starts to generate pseudo random integers
    #seed() can be used to set that starting point and generate reproducible random integers

    #eg
    random.seed(42)

    print(random.randint(1,10))
    print(random.randint(1,10))
    print(random.randint(1,10))

    #running it any number of time give the same sequence

print(random_mod())