
# tuples are immutable
# they can store values of any type.
t = ('a', 'b', 'a', 'c', 'd', 'e')
t = tuple()
print(t.count('a'))
print(t.index('c'))

for value in t:
    print(value)


name = tuple('eric',)
print(name)

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

#More soon
