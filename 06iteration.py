
# ITERATION presents us with the ability to run a block of code repeatedly
    # The while statement
    # for automating repetitve tasks
def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff')

countdown(3)


# Page 65
# Flow of execution
    # 1. Determine whether the condition is true or false
    # 2. if false, exit the while statement and continue execution at the next statement
    # 3. if condition is true, run the body and then go back to step 1


#Re-write the print_n() function using iteration (pg 66)
# ex2
def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n-1)

print_n('worla', 2)

print("\n")
def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1

print_n("mike", 3)

# 7.4 break -- helps jump out of a loop
while True:
    line = input('> ')
    if line == 'done':
        break
    print(line)


# 7.5 Square roots
    #Newton's method -- to know the square root of a, start with any estimate
    # x, you can compute a better estimate with the following formula
    # y = (x + a/x) / 2

a = 4; x = 3
y = (x + a/x) / 2
print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

# x = y
# y = (x + a/x) / 2
# print(y)

#Using iteration
while True:
    print(x)
    y = (x + a/x) /2
    if y == x:
        break
    x = y
