# source link: https://www.youtube.com/watch?v=WWm5DxTzLuk
# *args: arguments  e.g.: 1,2,3,"hello",True, etc.
# **kwargs: keyword arguments e.g.: x = 10, bool = False, etc.

# how can you implement a function that take unlimted arguments or keyword arguments?? 
# use *args or **args, actually * and ** plus any string would do, but the common standard syntax is args and kwargs!

print("______E X A M P L E 1: A R G S_____")
def ex1(*aa):
    for k in aa:
        print(k)
        
ex1(1,2,3,4,"^^ numbers [1 to 4]")
lst = [1,2,3,4,"^^ numbers [1 to 4]"]
ex1(*lst) # pass in a list as argument

print("______E X A M P L E 2: K W A R G S_____")
def ex2(x = 1, y = 10):  # if no value is passed in, x = 1 and y = 10
    print(x, y, x+y)
ex2()
ex2(2) # overriding one argument
ex2(y=20) # specify an arg to override
ex2(2, 20) # overriding both args
ex2(x = 2, y = 20) # you can be more specific if you have multiple args

# this gives you more freedome when implementing your functions. you don't  have to think about all possible input options. you work with what you have

print("______E X A M P L E 3: K W A R G S_____")
def ex3(**kwargs):  
    total = 0
    for elt in kwargs.items():
        total = total + elt[1]
        # kwargs.items() returns a tuple
    print(total)

ex3(x = 2, y = 20)

print("E X A M P L E 4: A R G S  &  K W A R G S")
def ex4(*args, **kwargs):  
    total1 = 0
    for elt in args:
        total1 = total1 + elt
    total2 = 0
    for elt in kwargs.items():
        total2 = total2 + elt[1]
        # kwargs.items() returns a tuple
    print(total1) # return 0 if we only pass in keyword arguments
    print(total2)

ex4(x = 2, y = 20)
