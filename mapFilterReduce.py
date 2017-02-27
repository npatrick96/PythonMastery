# 1. MAP: map is very useful when applying a function to all elements in a list.
items = [1, 2, 3, 4, 5]
def sqr(x): return x ** 2
print(list(map(sqr, items)))
# or we can use lambda
print(list(map((lambda x: x **2), items)))
# the 2nd argument of map can be a list of funtions 
def multiplyBy2(x):
    return (x*2)
def addOne(x):
    return (x+1)
funcs = [addOne, multiplyBy2]
for i in range(len(items)):
    val = list(map(lambda x: x(i), funcs))
    print(val)
    

# 2. FILTER: filter only returns elements for which the passed function is TRUE.
# filter is a builtin function, and therefore faster than a for loop.
nbrs = range(-5, 6)
print(nbrs)
neg_nbrs = list(filter(lambda x: x < 0, nbrs))
print(neg_nbrs)

# 3. REDUCE: from left to right, apply function to list, two elements at a time.
# Start by setting _acc to func(lst[0], lst[1]), and then to func(_acc, lst[2])
# example, finding the sum of all numbers in the [101, 1000] range - inclusive

_101to1000 = range(101, 1001)
print(_101to1000[0], _101to1000[-1])
from functools import reduce
_sum = reduce((lambda x, y: x + y), _101to1000)
print("sum: " + str(_sum))

