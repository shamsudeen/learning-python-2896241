# LinkedIn Learning Python course by Joe Marini
#

# import the math module, which contains features for working with mathematics
import math

# the math module contains lots of pre-built functions
print("The square root of 16 is", math.sqrt(16))

# in addition to functions, some modules contain useful constants 
print("Pi is:", math.pi)

# try some of the math functions for yourself here:

thestr = "Ogres are often foolhardy oafs"
newstr = ""
for i, c in enumerate(thestr):
    if c == "o":
        continue
    if i > 20:
        break
    newstr += c
print(newstr)

def inc(a,b=1):
    return(a+b)
a=inc(1)
a=inc(a,a)
print(a)


thestr = "This is a string"
print(thestr)
thestr = 5

try:
    x=int("five")
except ValueError:
    print("There is a value error.")
finally:
    print("Something went wrong.")

