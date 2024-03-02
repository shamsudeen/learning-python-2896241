# LinkedIn Learning Python course by Joe Marini
#


# TODO: import the math module, which contains features for working with mathematics
import  math

# TODO: the math module contains lots of pre-built functions

print(math.sqrt(9))   # square root of 9 is 3
print(math.pow(2,4))    # 2 raised to the power of 4 is 16

# TODO: use the round() function to round a number to the nearest integer
x = 5.789
y = round(x)
z = round(x, 0)
# TODO: in addition to functions, some modules contain useful constants 
print   ("Value of Pi: ", math.pi)

# TODO: demonstrate how to access specific parts of numbers using modulo (%) operator and floor division (//) operator
# TODO: demonstrate how to work with trigonometry functions
angle_radians = math.pi / 4
sine = math.sin(angle_radians)
cosine = math.cos(angle_radians)
tangent = math.tan(angle_radians)

print("Sine of pi/4: ", sine)
print("Cosine of pi/4: ", cosine)
print("Tangent of pi/4: ", tangent)

# TODO: demonstrate how to work with logarithmic calculations using the log() and exp() functions
base = 2
power = 8
logarithm = math.log(power, base)
exponent = math.exp (logarithm)

print("Logarithm of 8 to base 2: ", logarithm)

print("Log base 2 of  8: ", logarithm)
print("Exponential of Log base       2 of  8: ", exponent)    

# TODO: try some of the math functions for yourself here:
    #       - math.ceil(), rounds up if necessary (e.g., ceil(7.2) => 8)
    #       - math.floor(), rounds down if necessary (e.g., floor(7.2) => 7)
    #       - math.fabs(), returns the absolute value of its argument
    #       - math.trunc(), removes the fractional part of a number (e.g., trunc(7.2) => 7)     