
### ERRORS --
    # SYNTAX ERRORS - caused by developer. could be a misspelling or a typo in the code
    # ECEPTIONS - happind during code excecution

# exception handling
    # example
def divide_by(a, b):
    return a / b

 
    #example - good division
#print(divide_by(40, 4))


 
    #example - bad division
#print(divide_by(40, 0))

 
    #example - handling error - use a try catch block
#try:
#    print(divide_by(40, 0))
#except:
#    print("There was an error.")

 
    #example - more specific except statement
#try:
#    ans = divide_by(40, 0)
#except Exception as e:
#    print("Excecution Error!", e)
#    print(e.__class__)  # gives the type or class of error that occured.


    #example - more specific message to enduser
#try:
#    ans = divide_by(40, 0)
#except ZeroDivisionError as e:
#    print(e, " You cannot divide by zero.")


    #example - handling more than one error at a time.
try:
    ans = divide_by(40, 0)
except ZeroDivisionError as e:
    print(e, " You cannot divide by zero.")
except Exception as e:
    print(e, "Excecution Error")