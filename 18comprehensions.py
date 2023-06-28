### LIST COMPREHENSIONS
    #Syntax
    #[<expression> for x in <sequence> if <condition>] 
data = [2,3,5,7,11,13,17,19,23,29,31]

# Ex1: List comprehension: updating the same list
data = [x+3 for x in data]
print("Updating the list: ", data)

    # Regular for loop:
for x in range(len(data)):
    data[x] = data[x] + 3

# Ex2: List comprehension: creating a different list with updated values
new_data = [x*2 for x in data]
print("Creating new list: ", new_data)

# Ex3: With an if-condition: Multiples of four:
fourx = [x for x in new_data if x % 4 == 0 ]
print("Divisible by four", fourx)

# Ex4: Alternatively, we can update the list with the if condition as well
fourxsub = [x-1 for x in new_data if x % 4 == 0 ]
print("Divisible by four minus one: ", fourxsub)

# Ex5: Using range function:
nines = [x for x in range(100) if x % 9 == 0]
print("Nines: ", nines)

print("\n")
# Ex6: all possible permutations
x, y, z, n = 1, 1, 1, 2
pre_arr = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]
print(pre_arr)


### DICTIONARY COMPREHENSION

    #Syntax
    #dict = { key:value for key, value in <sequence> if <condition> } 
# Using range() function and no input list
usingrange = {x:x*2 for x in range(12)}
print("Using range(): ",usingrange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input list
numdict = {x:x**2 for x in number}
print("Using one input list to create dict: ", numdict)

# Using two input lists
months_dict = {key:value for (key, value) in zip(number, months)}
print("Using two lists: ", months_dict)



### SET COMPREHENSION
    #The set comprehension deals with the set data type and it's very similar to list comprehension.
    #The only key difference is the use of curly brackets for sets instead of square brackets as in lists.

set_a = {x for x in range(10,20) if x not in [12,14,16]}
print(set_a)

    #You can see the code format is similar to what I used in list comprehensions. For the sake of showing
    #versatility, I used the "not in" keywords to check the values in the list. The output is the values
    #in ranges 10 and 20 that are not present in that list.


### GENERATOR COMPREHENSION
    #Generator comprehensions are also very similar to lists with the variation of using curved brackets
    #instead of square brackets. They are also more memory efficient as compared to list comprehensions

data = [2,3,5,7,11,13,17,19,23,29,31]
gen_obj = (x for x in data)
print(gen_obj)
print(type(gen_obj))
for items in gen_obj:
    print(items, end = " ")


    #In the code above, I created a generator object of the class generator instead of a list. The elements
    #in this iterator object cannot be directly accessed and need the help of a for loop and as such,
    #I iterate over these elements and print them.



### Difference Between map() Function and List Comprehensions:
def square(num):
    return num * 2

newdata = map(square, data)

newdata = [x + 3 for x in data]


    #List comprehensions have been a relatively recent development but it does not necessarily mean they are
    #more efficient. Comprehensions have gained popularity primarily for providing cleaner code readability
    #and ease of use. They also provide some added advantages such as providing filtering using if else conditions.

    #List comprehensions also provide direct return of a list as compared to map() function that returns a map
    #object. It is mainly the clarity that has made list comprehensions popular, but map() functions are still
    # arguably a better choice when it comes to the use of larger sequences.