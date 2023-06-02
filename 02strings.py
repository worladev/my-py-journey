# A sequence of characters
    #characters can be accessed one at a time with the bracket operator
fruit = 'banana'
letter = fruit[0]

firstWord = "I cannot stop "\
    "until i win."
print(firstWord)

secondWord = "Watch me."

print(firstWord + secondWord)

# Multiline string
address = """422 Long Lane Road
Newtown
Jungle Avenue"""

print(address)


# 8.2 len() function
count = []
for i in range(len(secondWord)):
    count += [i]
    i += 1
print(count)

# 8.3 Traversal with a for and while loop
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index += 1

print('\n') 

### Print string backwards
def backward_string(str):
    index = len(str)
    while index > 0:
        letter = str[index - 1]
        print(letter)
        index -= 1

backward_string('worla')

# 8.4 String slices
    # a segment of a string is called a slice.
    # [n:m] returns the part of the string from the n-eth character to
    # the m-eth character, including the first but excluding the last.
    # if you omit the first index (before the colon), it starts at the beginning
    # if you omits the second index, it goes to the end.
sample = 'Monty Python'
print(sample[0:5])
print(sample[0:0])


# 8.6 Searching
def find(word, letter):
    index = 0
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1
#exx page 75

# 8.7 Looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count += 1
print(count)

#ex page 75

# 8.8 String methods
    # .upper()
    # .lower()
    # len()
    # .capitalize()
    # .strip()
    # .title()
    #
new_word = word.upper()

# 8.9 The in operator
def in_both(word1, word2):
    for letter in word1:
        if letter in word2:
            print(letter)

in_both("michaelson", "jungleton")

