# FUNCTIONS
## import math

# A named sequence of statements that performs a computation.
# Define a function by specifying a name and a sequence of statement
    # this function can be called later by name.

type(40)        #name of this function is type
type(3.44)      #the expression in the parentheses is called the argument
type(True)      #this function returns the type of the argument
type('Hi')

# It is very common for a function to "take" an argument and "return" a result
    #the result is known as the return value

#python provides function that converts values from one type to another.
str() #convert it's argument to string

int() #if it can't, it throws an exception.

#int('Hello')    #throws a ValueError:
#int can convert a floating point value to an integer by chopping off the fraction part

num = int(3.14)
print(num)

print(int(3.14))

#float converts integers and strings to floating-point numbers
float(32)
float('3.554')


### MATHS FUNCTIONS
    # Python has a math module -- a module is a file that contains a collection of related functions
    # To use a function in a module, import the module using the import statement.
    
#print(math)

    # We use the dot notation to access the functions in a module

## COMPOSITION
    #The most useful features of programming languages is the ablility to take small 
    # blocks and compose them.
    # for example, mathematical expressions can be arguments of a function or even function call
    #Page 19

## ADDING NEW FUNCTIONS
def newLyrics():
    print('Hello hello all in hays')
#def is a keyword that indicates function definition
#the name is newLyrics
#same as naming a variable.
#empty parentheses means it doesn't take any arguments when calling it.
#first line is called the header and the rest is the body.
#functions can be called inside another functions.
#avoid functions and variables with the same name.

def allLyrics():
    newLyrics()
    newLyrics()

allLyrics()

## FLOW OF EXECUTION
    # from top to down

## PARAMETERS AND ARGUMENTS
def print_username(username):
    print(username * 3)

print_username('worlasi ')

name = 'whois '
print_username(name)

#arguments can be a variable, an expression or another function


###LOCAL VARIABLES AND PARAMETERS
    #variables created inside a function is local.
    #meaning it only exist inside the function
def displayFullname(firstname, lastname):
    fullname = firstname + lastname
    print_username(fullname)

name1 = 'Worlasi '
name2 = 'Kokobi '

displayFullname(name2, name1)



###FRUITFUL FUNCTIONS AND VOID FUNCTIONS
    #Functions that return results
    #Functions that don't return a value. void functions might
        #display something on the screen or have some other
        #effect but they don't have a return value.
        # if result is assigned to a variable, it returns None

result = print_username('loli ')
#print(result)


#### EXERCISE ####
# 3.1
def right_justify(s):
    print(' ' * (70 - len(s)) + s)

right_justify('me')

# 3.2

def print_length(word):
    uopeople = len(word)
    print(uopeople)

def call():
    print_length('worla')
    print_length('Eric')
    print_length('elephant')

call()
call()

x = 5
y = 3
x + y
'x + y'

percentage = (60.0 * 100.0) / 55.0
print(percentage)

print((1,000,000))