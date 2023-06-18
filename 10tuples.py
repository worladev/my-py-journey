### CHECK AGAIN

# Two ways to declare a tuple
# () - parenthesis
# tuple() - in-built function

# tuples are immutable
# they can store values of any type.


# for value in t:
#     print(value)

name = ('eric',)
name1 = tuple('eric')
print(name)
print(name1)

z = ('eric',)


## 12.4 TUPLE ASSIGNMENT
    # conventional swap assignment
a = 5
b = 10

temp = a
a = b
b = temp

    # tuple assignment
a, b = b, a

# Tuple supports slicing

# Unpacking
points = (5, 7, 10)
x, y, z = points
k, j, *other = points

print(x, y, z)
print(other)

# Tuple methods count(), index()
names = ("Andy", "Enoch", "Sam", "Worlasi", "Andy", "Sam")
print(names.count('Andy'))
print(names.index("Sam"))

t1 = "a", "b", "c", "d", "a"  # - without the bracket
t = ("a", "b", "c", "d", "e")
print(t.count('a'))
print(t.index("a"))
