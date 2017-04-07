#! /usr/bin/env python3

# From source: https://docs.python.org/3/library/functools.html

# The functools module is for higher-order functions: functions that act on or return other functions. In general, any callable object can be treated as a function for the purposes of this module.

# The functools module defines the following functions: 
### cmp_to_key(func)
### lru_cache(maxsize=128, typed=False)
### total_ordering
### partial(func, *args, **keywords)
### partialmethod(func, *args, **keywords)
### reduce(function, iterable[, initializer])
### singledispatch(default)
### update_wrapper(wrapper, wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)
### wraps(wrapped, assigned=WRAPPER_ASSIGNMENTS, updated=WRAPPER_UPDATES)

# As most of these are complex, I am going to focus on reduce.

## Reduce takes two required arguments (function and iterable) and one optional arguement (initializer)

## E X A M P L E 
from functools import reduce # you wouldn't need this line in python2
# for a python2 example and more detailed explanation of the use of reduce,  
# check this link: 
# https://github.com/npatrick96/PythonMastery/blob/master/mapFilterReduce.py 

A = [1, 2, 3, 4, 5]
# to calcuate the sum of list A, do the sum like this ((((1+2)+3)+4)+5) 
# start by setting the accumulator x to A[0], and then x = x + y, y being the next value in the sequence.
print(reduce(lambda x, y: x+y, A))
# setting the accumulator to 10, returns the previous sum plus 10
print(reduce(lambda x, y: x+y, A, 10))







print("____________")

import sys
print(sys.version)