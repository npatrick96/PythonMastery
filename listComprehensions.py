# the following is based on the tutorials notes from https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions

# instead of using loops, we can use list comprehensions

squares  = []
for i in range(10):
    squares.append(i**2)
print (squares)

# the above can be achieved in just two lines of code using list comprehensions

squares = [x**2 for x in range(10)]
print (squares)

# more can be done with list comprehensions such as combining elements of two list into tuples

results = [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
print (results)

# more can be done using list comprehensions: calling a method on all elements of a list or creating a new list.

squarePairs = [(x, x**2) for x in range(6)]
print(squarePairs)

vec = [-4, -2, 0, 2, 4]
print([x*2 for x in vec])
print([x for x in vec if x >= 0])

# list comps can also be used to flatten lists of lists

vec = [[1,2,3], [4,5,6], [7,8,9]]
print([num for elem in vec for num in elem])
#print([elt for elt in  lst for lst in vec]) # doesn't work!!
