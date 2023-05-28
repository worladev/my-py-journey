### VARIABLES  are simply places to store informaton and to give that
    #information a name.
    #as the term indicates the information stored is "variable",
    #meaning that it can change.
### EXPRESSIONS are combinations of values, variables, and operators
    #that the Python interpreter evaluates to compute a resulting value
### STATEMENTS are units of code that have an effect, like creatig a
    #variable or displaying a value. The Python interpreter executes
    #statements to produce the effect.(When executing a statement, the 
    # the interpreter evaluates any expressions included in the statement)
### FUNCTIONS


#https://studystacks.herokuapp.com/
# ASSIGNMENT STATEMENTS
# Creates a new variable and gives it a value.

### VARIABLES
age = 27               #integer
comp = 3 + 6j          #complex
name = 'worlasi'       #string
cost = 50.43           #double
isloggedin = True      #boolean
print(age)

### DATA TYPES ###
# Numeric (integer, float, complex number)(+, -, *, **, /, //, %)
# Sequence (string, list, tuples)
# Boolean
# Dictionary
# Set


# Multple declaration on one line.
age1,name2,age3 = 11, "Mike", 13
# Using string formating
print(f"{age1} {name2} {age3}")
# Normal print statement
print(age1)
print(name2)
print(age3)

# variable names cannot begin with a number
# you can use underscore/camelCase when naming a variable
# Python keywords cannot be used (page 10)


### EXPRESSIONS AND STATEMENTS
# Expression is a combination of values, variables and operators

# Statement is a unit of code that has an effect like creating
    # a variable or displaying a value


## ORDER OF OPERATIONS
# PEMDAS
# Parentheses, Exponentiation, Multiplication, Division
    # Addition, Subtraction

print(1 + 2**3)



## STRING OPERATION
    # can't perform mathematical operations on strings
    # two exceptions + and *
    # + performs string concatenation
    # * performs repetition


## COMMENTS


## DEBUGGING
    #Three kinds of errors
    # Syntax error -- structure of a programs and rules
        #about that structure.
    # Runtime error -- error only appears after the program
        #has started running. (also called exceptions)
    # Semantic error -- related to meaning



## EXERCISE ##
    # 2.2
# 1
pi = 3.14
raduis = 5**3
const = 4/3

volume = const * pi * raduis
print(volume)

# 2
coverPrice = 24.95

print('\n')