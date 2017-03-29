# SOURCES
# 1. https://www.youtube.com/watch?v=FsAPt_9Bf3U
# 2. https://www.youtube.com/watch?v=fVon4QaY4wo
# 3. http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/


# first class functions allow us to treat functions as any other objects
# closures allow us to take advantage of first class functions and return an inner fucntion that remember and have access variables local to the scope in which they were created
# nested functions are functions that are declared within other functions
# defining functions within functions is a weird concept. It is like func-inception but useful! 
print("____________E X A M P L E 1____________")
def outside(x=5):
    def printHello():
        print (x)
        #print ("Hello")
    return printHello()


myFunc5 = outside() 
myFunc7 = outside(7)  
# print(myFunc5)
# print(myFunc7)

# the above line works even though the variable x is not passed into printHello
# python is treating the function as a class, thus all functions defined within it have access to its variables
# nested functions are however better than classes as they are easier to implement (less code to type)
# in nested loops, you also don't have to specify which function to call, you can some conditional statements when implementing to take care of that beforehand

print("____________E X A M P L E 2____________")
def addOneOuter(myFunc):
    def addOneInner():
        return myFunc() + 1
    return addOneInner()
    
def returnThree():
    return 3
    
finalFunc = addOneOuter(returnThree)
print(returnThree(), finalFunc)

# This second example shows the basic structure of a decorator in Python. You can use nested loops to set up a decorator on a function so that you can override it or change how it behaves after you implement. This is useful when dealing with large functions in case you don't want to break or modify their inner structures but you want to modify their outputs by simply adding external code to take care of that.

# For example if wanted from now to make returnThree return 4, we can apply the addOneOuter function to it, and that would take care of that.

# This concept of decorators and nested functions is heavily used in Haskell, an awesome purely functional language that every Python programmer ought to check out at some point. #JustSaying!

returnThree = addOneOuter(returnThree)
print(returnThree) # returnThree is printing 4!

# As you can see, the above works but it is kind of tedious and confusing at the same time, especilly Line 17. To avoid this, python has an asesome syntax that handles.

@addOneOuter
def returnThree():
    return 3
    
print(returnThree) # this line should print 4!

# That END. For more, check the links at the top. Thanks! 

# N O T E: the code in this file was tested using Python 2.7.10. If it doesn't work on your machine, use the below commented lines to verify which version of Python you are using! You know, just in case!

# print("____________")
# 
# import sys
# print(sys.version)
# 
# print("____________")
# 
# import platform
# print(platform.python_version())






