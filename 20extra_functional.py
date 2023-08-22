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
# in-built tranformation function

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


# user defined transformation function
def square(number):
    return number ** 2

numbers = [1, 2, 3, 4, 5]

squared = list(map(square, numbers))

print(squared)

