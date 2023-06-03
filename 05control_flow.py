## MATH OPERATORS
    # +     addition
    # -     subtraction
    # /     division
    # *     multiplication

## LOGICAL OPERATORS
    # and, or, not
    # and : both expressions must evaluate to True
    # or : only one of the expression should evaluate to True
    # not : negates a boolean expression
x = 5
y = 6
value = not (x > y)
print(value)

#Any nonzero number is interpreted as True in python
 #Relational operators
    # !=
    # >
    # <
    # >=
    # <=
    # ==

# FLOOR DIVISION ##
    # The Floor division operator, //, divides two numbers and rounds down
        # to an integer
minutes = 60
hours = minutes // 60

#to get remainder
remainder = minutes - hours * 60

#alternatively, use the modulus
remainder = minutes % 60

#another use of modulus is to check whether one number is divisible by another
    # if x % y is zero, then x is divisible by y

# to extract righ-most digit x % 10
# x % 100 yields the last two digits
print(200 % 100)


### BOOLEAN EXPRESSIONS ###
    # An expression that is either true or false. 
    # True and False are special values that belong to the type bool; they are not strings
five = 5
seven = 7
print(five == seven)
print(type(False))


## CONDITIONAL EXECUTION ###
    # if
    # else
    # elif

    # To write useful programs, we check conditions and change the behaviour of
        # the program accordingly

    # if statements have same structure as function definitions
    # a header followed by an indented body(compound statements)
if x < 0:
    pass    #TODO: handle negative values!

    # light example
current = False

if current:
    current = False
    print("Turning off light")
    
if not current:
    current = True
    print("Turning on light")
     

    # Alternative Execution (else / branches) ##
if x % 2 == 0:
    print('even')
else:
    print('odd')

    # Chained Conditionals ##
    # more than two possibilities requires more than two branches.
if x < y:
    print('less than')
elif x > y:
    print('greather than')
else:
    print('equals')

    # only the first true branch runs in a conditional check

    # Nested Conditionals (condition inside a condition)


## match statements
http_status = 200

match http_status:
    case 200:
        print("Success")



## LOOPS
    # for loop
    # while loop
        #break
        #continue
        #pass

#iterate and print index and item.
favorite_movies =['chuck pipper', 'uncharted', 'quiver', 'killer bean', 'minions']

for indx, item in enumerate(favorite_movies):
    print(indx, item)

    # nested loops
    # outter loop
for i in range(2):
    #inner loop
    for j in range(5):
        print(0)
    print()



### RECURSION ###
    # a function calling itself
# ex1
# def countdown(n):
#     if n <= 0:
#         print('Blastoff!')
#     else:
#         print(n)
#         countdown(n-1)


# ex2
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n('worla', 2)

# attempt exercise on page 44

### Infinite Recursion ###

### KEYBOARD INPUT ###

####LEARNING Jour####
# No1
def countdown(n):
    if n <= 0:
        print('Blastoff!')
    else:
        print(n)
        countdown(n-1)

def countup(n):  #function definition
    if n >= 0:      # if conditional to check if number is greater or equal to 0 and print blastoff, else, print the number and call the countup() function with an argument of n+1 which means to increase the number by 1
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

def user_input(choice): #a function that takes user input as argument and call either the countdown or countup function based on the number the user entered.
    if choice >= 0:
        countdown(choice)
    else:
        countup(choice)

user_choice = int(input('input a number\n')) #a variable that is asigned the user's input.

print('Output')
user_input(user_choice) #calling the user_input function and passing the user's input as an argument.

# No2
#this is a funtion that accepts a value argument and compares it to zero
    #if the value is greater than zero, the value is divided by zero and the result printed.
    # else, the value is printed.
def runtime_error(value):
    if value > 0:
        print(value / 0)
    else:
        print(value)

runtime_error(-3)

#this code only generates a runtime error if the value it takes as an argument is a positive number and it is greater than 0.
#NOTE: negative values will work just fine.

#the error generated upon the function taking a positive value argument is called
    #ZeroDivisionError: division by zero
    #this simply means a number cannot be divided by zero thereby raising an undefined status in most mathematical concepts.
    #to fix this error, you only need not to use a 0 as a divisor in your mathematical operations.


### DISCUSSION ###
    #Chained conditionals are used if there are more than one condition to check for and may result in multiple branches.
def name_lenght_guess_game(name):
    if len(name) <= 3:
        print('Guess: Your name contains 0 to 3 letters.')
    elif len(name) <= 6:
        print('Guess: Your name contains 4 to 6 letters')
    elif len(name) <= 9:
        print('Guess: Your name contains 7 to 9 letters.')
    else:
        print('Guess: Your name is longer than 9 letters.')

name_lenght_guess_game('confidence')
name_lenght_guess_game('eri')

    #Nested conditionals are implemented if further conditions are needed to validate the outer condition or perform further checks.
    # a conditon inside another condition. the inside condition often check for another true value different from the outer one.

x = 44
if x % 5 == 0:
    if x > 15:
        print(x, 'is greater than 15 and is a multiple of 5.')
    else:
        print("Try again.")
else:
    print('Invalid number entered.')


## No3
x = 44
if x % 5 == 0:
    if x > 15:
        print(x, 'is greater than 15 and is a multiple of 5.')
    else:
        print("Try again.")
else:
    print('Invalid number entered.')


x = 45
if x % 5 == 0 and x > 15:
    print(x, 'is greater than 15 and is a multiple of 5.')
else:
    print('Invalid number entered.')

    