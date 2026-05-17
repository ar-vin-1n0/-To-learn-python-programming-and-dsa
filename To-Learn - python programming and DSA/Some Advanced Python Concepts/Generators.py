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