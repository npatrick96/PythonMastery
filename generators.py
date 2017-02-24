# when and why to use generators instead of list

# WHY:
# save space - a generator is not holding all values in memory
# it is waiting for a loop, and returns value one at a time 
# this results in increasead perfomance and reduced computation times
# generators are useful when dealing with large datasets

# WHEN TO USE THEM: everytime!!! ^^^ YAY, because *perfomance* !!
# they are also more clean and easily readable

# SOURCES
# https://www.youtube.com/watch?v=bD05uGo_sVI
# https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Generators


# suppose we are given nums_lst and we are asked to sqaure all its elts
nums_lst  = [1, 2, 3, 4, 5]

# the following function uses a list to store results 
def squareElts(nums):
    sq = []
    for i in nums:
        sq.append (i*i)
    return sq
sq_lst = squareElts(nums_lst)
print(sq_lst)

# a generator is like a function, except the keyword YIELD is used in place of RETURN    
# using a generator method, we can get rid of the temp sq list
def squareElts(nums):
    for i in nums:
        yield (i*i)
sq_lst = squareElts(nums_lst)
print(next(sq_lst)), print(next(sq_lst))
print() # print empty line after first two elts in generator object
for i in sq_lst:
    print(i)
    
# the above can be easily written as a list comprehension
sq_lst = [x * x for x in nums_lst]
print(sq_lst)

# by replacing the outside brackets,sq_lst would be a generator
sq_lst = (x * x for x in nums_lst)
for i in sq_lst:
    print(i)
