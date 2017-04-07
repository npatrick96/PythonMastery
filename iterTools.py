#! /usr/bin/env python3

# I. INFINITE ITERATORS 
from itertools import count, cycle, repeat
# I.1. count()
countFromOne = count(1)
for i in range(10):
    print(next(countFromOne))

# I.2. cycle()
print("____________")
cycleABC = cycle("ABC")
for i in range(9):
    print(next(cycleABC))

# I.3. repeat()
print("____________")
def repeat_Elt_n_times(elt, n):
    return repeat(elt, n)
repeat_A_3_times = repeat_Elt_n_times("A", 3)

for i in range (3):
    print(next(repeat_A_3_times))

# More documentation on itertools can be found at https://docs.python.org/3/library/itertools.html




print("____________")

import sys
print(sys.version)