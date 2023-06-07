
# Built-in type
# A list is a sequence of values. the values can be any type.
# The values in a list are called elements.
# A list within another list is nested

cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [44, 234]
empty = []

#List are mutable
cheeses[0]

numbers[1] = 5

# the in operator
5 in numbers

'Edam' in cheeses

## 10.3 TRAVERSING A LIST
for cheese in cheeses:
    print(cheese) # to read elements

# one way is to use range and len
# to write or update elements
for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2

# 10.4 LIST OPERATION
    # the + operator
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)

    # the * operator repeats a list a given number of times
print(a * 3)


### 10.4 LIST SLICES
# slice works on lists as well
# always make a copy before modifying a list

## 10.6 LIST METHODS
    # .insert() add a new item at a specified point in the index
    # .append() adds a new element to the end of a list
    # .extend() takes a list as an argument and appends all of the elements
    # .sort() arranges the elements of the list from low to high

    # most list methods are void, they modify the list and return None


## 10.7 MAP, FILTER and REDUCE
    # to add up all the numbers in a list, you can use a loop like this
def add_all(t):
    total = 0
    for x in t:
        total += x
    return total

    # built-in function sum() to add all the numbers in a list.
g = [5, 2, 3]
total = sum(g)
print(total)

    # traversing a list while building another
    # Example --takes a list of stings and return a list that contains a
    # capitalized string.
def capitalize_all(t):
    res = []
    for s in t:
        res.append(s.capitalize())
    return res

    # select some of the elements from a list and return a sublist.
    # Example -- takes a list of strings and returns a list that contains only
    # the uppercase strings.
def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res


# 10.8 DELETING ELEMENTS
# pop(index) modifies the list and returns the element that was removed.
    # if no index is provided, it deletes and returns the last element.
# del operator -- if you don't need the removed value.
# remove(value) -- if you know the element but not the index -- remove returns None
# del with slice index -- to remove more than one element.


# 10.9 LIST and STRINGS
    # to convert from a string to a list.
    # the list function breaks a string into individual letters 
s = 'spam'
t = list(s)
print(t)


    # to break a string into words, use split
s = 'pining or the jags'
t = s.split()
print(t)

    # an optional argument called delimiter specifies which characters to use as word boundaries.
s = 'spam-spam-spam'
delimiter = 'a'
t = s.split(delimiter)
print(t)

    # join is the inverse of split -- it takes a list of strings and concatenate them
t = ['pining', 'for', 'the', 'jags']
delimiter = ' '
s = delimiter.join(t)
print(s)
print("This is it")



# 10.10 OBJECTS and VALUES
a = 'banana'
b = 'banana'
    # 2 cases
        #1 a and b both refer to different objects with same value
        #2 they refer to the same object.
        # use the is operator to check for sure
print(a is b)
    # creating two list with same value gives two objects


#10.11 ALIASING
    # reference -- associating a variable with an object

#10.12 LIST ARGUMENTS
    # when you pass a list to a function, the function gets a reference to the list
# example
def delete_head(t):
    del t[0]

letters = ['a', 'b', 'c']
delete_head(letters)
print(letters)
    # the parameter t and the variable letter are aliases for the same object.
    # append modifies a list.
    # the + operator creates a new list. the original list will be unchanged.


# 10.13 DEBUGGING
    # most list methods modify the argument and return None
    # it is the opposite for string methods
    







