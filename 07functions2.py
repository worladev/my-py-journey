
### VARIABLE SCOPE
    # Built-in --reserved keywords python use for it's built-in functions (def, print, for, in)
    # Global -- declared outside a function and can be accessed from anywhere
    # Enclosed -- a variable declared in a funtion inside a function/nested function
    # Local -- a variable declared inside a function

### FRUITFUL FUNCTIONS ###
    
    ## 6.1 Return Values    
    # functions that returns a value
import math

def area(radius):
    a = math.pi * radius ** 2
    return a

#Sometimes, its useful to have multiple return statements
#example
def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x

#A code that appears after a return statement, or any other place that
    #flow of execution cannot reach is called a dead code.

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result


#Exercise
def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

# print(compare(2, 4))
# print(compare(4, 4))
# print(compare(2, 1))


    ## 6.2 Incremental Development page 54

#Exercise
#STAGE 1 --- define a function with the lengths as parameters and returns 0
def hypotenuse(length_a, length_b):
    return 0.0

print(hypotenuse(1, 2))

#STAGE 2 --- takes the square of the length and save it in a local variable
def hypotenuse(length_a, length_b):
    length_a_squared = length_a**2
    length_b_squared = length_b**2
    print(length_a_squared)
    print(length_b_squared)
    return 0.0

print(hypotenuse(1, 2))

#STAGE 3 --- adds the squared length and assign it to a local variable
def hypotenuse(length_a, length_b):
    length_a_sqrd = length_a**2
    length_b_sqrd = length_b**2
    add_length_sqrd = length_a_sqrd + length_b_sqrd
    print(add_length_sqrd)
    return 0.0

print(hypotenuse(1, 2))

#STAGE 4 --- returns the square root of the final result.
def hypotenuse(length_a, length_b):
    length_a_sqrd = length_a**2
    length_b_sqrd = length_b**2
    add_length_sqrd = length_a_sqrd + length_b_sqrd
    result = math.sqrt(add_length_sqrd)
    return result

print(hypotenuse(8, 2))


## 6.3 Composition

#A function that takes two points.
    # the center of the circle
    # point on the perimeter
#and computes the area of the circle

#Assume center point is stored in xc and yc
    #perimeter point is in xp and yp

#Step 1 : find the radius of the circle (distance between 2 points)
#step 2 : find the area of a circle with that radius

def circle_area(xc, yc, xp, yp):
    radius = distance(xc, yc, xp, yp)
    result = area(radius)
    return result

#OR -- concise implementation
# def circle_area(xc, yc, xp, yp):
#     return area(distance(xc, yc, xp, yp))


## 6.4 Boolean functions

#Functions can return booleans (used to hide complicated tests inside functions)
#Example
def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

print(is_divisible(6, 3))

#OR -- concisely
# def is_divisible(x, y):
#     return x % y == 0

#Boolean functions are often used in conditional statements
# if is_divisible(x, y):
#     print('x is divisible by y')


#Exercise
def is_between(x, y, z):
    if y >= x and y <= z:
        return True
    else:
        return False

#OR -- concisely
def is_between(x, y, z):
    return y >= x and y <= z

print(is_between(4, 5, 6))


## 6.5 More Recursion
#Example 1 Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result


#Example 2 Fibonacci
def fibonacci(n):
    if not isinstance(n, int):
        print('Factorial is only defined for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers.')
        return None
    elif n == 0:
        return 1
    else:
        return n * fibonacci(n-1)

#NOTE : don't follow the flow of execution, take a leap of faith

print(fibonacci(-4))

## 6.8 Checking Types
