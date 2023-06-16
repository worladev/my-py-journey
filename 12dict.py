
### Dictionary is like a list but more general.
    # in a list, the indices are integers
    # in dictionaries, they can be any type

    # contains a collection of indices called keys, and a collection of values
    # the association of a key and a value is called a key-value pair or an item.

# creates an empty dictionary with no items.
eng2sp = dict()
eng2sp['one'] = 'uno'
print(eng2sp)

# the len(value) function works on dictionaries
# the in operator works on dictionaries; it returns the number of key-value pairs

valueIn = 'one' in eng2sp
print(valueIn)

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


r = histogram('confidence')
print(r)



## 11.3 LOOPING AND DICTIONARIES
def print_hist(h):
    for c in h:
        print(c, h[c])


h = histogram('parrot')
print_hist(h)

# for sorted order
for key in sorted(h):
    print(key, h[key])



## 11.4 REVERSE LOOKUP
    # a function that takes a value and returns the first key that maps to that value.
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('No such key in dict.')

# successful example
h = histogram('parrot')
key = reverse_lookup(h, 2)
print(key)

#key = reverse_lookup(h, 3)
#print(key)



## 11.5 DICTIONARIES AND LISTS
# a function that inverts a dictionary
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse)

# page 108 (discussion assignment)
# a hash is a function that takes a value (of any kind) and returns an integer.


# 11.6 MEMO
    # improved fibonacci
known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res


print(8^2)

