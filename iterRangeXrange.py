# iter() returns an iterator retuns a next() or raises a StopIteration error

ss = "ok"
s = iter(ss)

print(s.next())  # print "o"
print(s.next())  # print "k"
#print(s.next())  # "StopIteration" error

'''
#https://docs.python.org/2/library/functions.html#iter

One useful application of the second form of iter() is to read lines of a file until a certain line is reached. The following example reads a file until the readline() method returns an empty string

with open('mydata.txt') as fp:
    for line in iter(fp.readline, ''):
        process_line(line)     
'''

# if you are reading this, you probably know how to use range(), e.g.:
for i in range(10, 0, -1): # start at 10, end before reaching 0, increment by -1
    print ("i is " + str(i))

# but, did you know you can use range() to create with a list, check out this:
lst = range(10, 0, -1) # this creates a list as does every call of range()
print(lst)

'''
range(start, stop[, step]) # https://docs.python.org/2/library/functions.html#range
This is a versatile function to create lists containing arithmetic progressions. It is most often used in for loops. The arguments must be plain integers. If the step argument is omitted, it defaults to 1. If the start argument is omitted, it defaults to 0. 
'''

xrange_ = xrange(10, 0, -1)  # this does not create a list but an xrange() object
print(xrange_)

'''
# http://stackoverflow.com/a/94962/6476668 
range() creates a list, so if you do range(1, 10000000) it creates a list in memory with 9999999 elements.

xrange is a sequence object that evaluates lazily.
xrange is nto exactly a generator but it evaluates lazily and acts like a generator. 
xrange(x).__iter__() is a generator.

'''


