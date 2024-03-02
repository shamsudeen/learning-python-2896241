# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# re-declaring a variable works
myint = "abc"
print(myint)
# to access a member of a sequence type, use []
print(mylist[2])
print(mytuple[1])
# accessing a dictionary value uses the key as an index
print(mydict["one"])

# you can also iterate over sequences using loops
for item in mylist:
    print(item) 

# Tuples are immutable - they cannot be changed once created
try:
    mytuple[0] = 99
except TypeError as e:
# tuples are immutable and can't be changed
# use slices to get parts of a sequence
    print(mylist[1:5])
    print(mylist[1:5:2]) # this gets every second element starting from the first one
    
# dictionaries have keys that must be unique but can contain mixed types for values
different_types = {True : "Yes!", 42 : "The Answer", "Python" : "Is fun!"}
for key,value in different_types.items():
    print("{}: {}".format(key, value))

# you can use slices to reverse a sequence
print(mylist[::-1])
# dictionaries are accessed via keys
print(mydict["one" if True else "zero"])
# conditional expressions (ternary operator) return the last expression if no condition is met

# ERROR: variables of different types cannot be combined
print("string type" + str(123))
# Global vs. local variables in functions
def someFunction():
    x = 78
    y = 65
    z = x * y
    w = "Hello World"
    v = "Goodbye Cruel World"
    return z,w,v
result = someFunction()
print(result)
# Scope rules apply when referencing variables inside functions
# If a variable isn’t defined within the function it will look upwards in the scope chain until it finds the variable or hits the top
print(x) # error because 'x' not defined outside function scope

# Recursion is when a function calls itself
def factorial(n):
    """Calculate the factorial of n"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n -     1)   # <-- here is where it calls itself
                                          #       again with a smaller argument
print(factorial(5))

# Loops are more common than recursion
def fibonacci(n):
    """Return the nth Fibonacci number"""
    a, b = 0,  1
    count = 0
    while count < n:
        a, b = b, a+b
        count += 1
    return a
print(fibonacci(9))

# Functions can also take multiple arguments
def greetings(name, title="Mr."):
    print(title + ", " + name)
greetings("John")
greetings("Jane", "M    rs.")
# Scope of Variables
# someFunction
# someFunction()
# print(mystr)

# del mystr
# print(mystr)