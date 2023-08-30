'''
map()
--> a built-in function that allows to process and transform all the items
in an iterable without using an explicit for loop, a technique commonly
known as mapping.

Mapping consists of applying a transformation function to an iterable to
produce a new iterable. Items in the new iterable are produced by calling
the transformation function on each item in the original iterable.

Three commonly used techniques to process data functionally:
- Mapping --> consists of applying a transformation function to an iterable to
produce a new iterable. Items in the new iterable are produced by calling the
transformation function on each item in the original iterable.

- Filtering --> consists of applying a predicate or Boolean-valued function to
an iterable to generate a new iterable. Items in the new iterable are produced
by filtering out any items in the original iterable that make the predicate
function return false.

- Reducing --> consists of applying a reduction function to an iterable to produce
a single cumulative value.

SYNTAX: map(function, iterable[, iterable1, iterable2,..., iterableN])
            ==>function -- any type of python callable that takes an argument and returns a concrete and useful value.
'''

# ==> in-built tranformation function

#Example
# converting string numbers to integers
str_nums = ["3", "5", "2", "8", "3", "4"]
int_nums = set(map(int, str_nums))
print(int_nums)

# getting absolute values
numbers = [-2, -1, 0, 1, 2]
abs_values = list(map(abs, numbers))
print(abs_values)

# converting to floating point numbers
flo_nums = list(map(float, numbers))
print(flo_nums)

# getting the length of words in a list
words = ["Come here", "Welcome", "Hello Python"]
word_len = list(map(len, words))
print(word_len)

# ==> If you supply multiple iterables to map(), then the transformation function
# must take as many arguments as iterables you pass in. the iteration stops at
# the end of the shortest iterable.  
#Example
l1 = [1, 2, 3]
l2 = [2, 3, 4, 5]

# pow() takes two arguments x and y and returns x to the power of y.
power = list(map(pow, l1, l2))
print(power)


# ==> Transforming iterables of strings with map()
#using str method
string_list = ["processing", "strings", "with", "map"]
capitalize = list(map(str.capitalize, string_list))

upper = list(map(str.upper, string_list))

lower = list(map(str.lower, string_list))

title = list(map(str.title, string_list))


# ==> Removing Punctuation
#a custom function that removes punctuation using regular expression
#implement using sub() regular expression function in the re module
import re

def remove_punctuation(word):
    return re.sub(r'[!?.:;,"()-]', "", word)

print(remove_punctuation("...!Python."))

#using map() to remove punctuation from a list of words
text = '''Some people, when confronted with a problem, think
"I know, I'll use regular expressions."
Now they have two problems. Jamie Zawinski'''

words = text.split()

remove_punct = list(map(remove_punctuation, words))
print(remove_punct)



# ==> user defined transformation function
def square(number):
    return number ** 2

numbers2 = [1, 2, 3, 4, 5]

squared = list(map(square, numbers2))

print(squared)

#or using lambda
squared = list(map(lambda num: num ** 2, numbers2))
print(squared)


